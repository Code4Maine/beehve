from datetime import datetime, timedelta
import pytz
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation

from honey.models import Project, ProjectCommit

from gittle import Gittle

class Command(BaseCommand):
    help = 'Grabs the latest commits for a project and creates relevant buzzes \
            when found.'

    def handle(self, *args, **options):
        projects = Project.objects.all()

        for project in projects:
            if project.git_url:
                repo_path = '/tmp/' + project.slug
                try:
                    repo = Gittle(repo_path, project.git_url)
                except Gittle.NotGitRepository:
                    try:
                        repo = Gittle.clone(project.git_url, repo_path)
                    except:
                        # put some logging here
                        pass
                if repo:
                    new_commits = []
                    for commit in repo.commit_info():
                        try:
                            prev_commit = repo.get_previous_commit(commit['sha'])
                            time = (datetime.fromtimestamp(commit['time']) + timedelta(commit['timezone']/(60*60))).replace(tzinfo=pytz.utc)
                            if commit['message'][:-1] != commit['summary']:
                                summary = commit['summary']
                                message = commit['message']
                            else:
                                message = commit['summary']
                                summary = 'Commit {0} was pushed.'.format(commit['sha'][:15])
                            pcommit = ProjectCommit.objects.create(
                                project=project,
                                chash=commit['sha'],
                                message=message,
                                summary=summary,
                                author=commit['author']['raw'],
                                created=time,
                                time=time,
                                diff=repo.diff(commit['sha'], prev_commit).next()['diff']
                            )
                            new_commits.append(pcommit)
                        except:
                            pass