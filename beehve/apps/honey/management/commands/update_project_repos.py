from datetime import datetime, timedelta
import pytz
from django.core.management.base import BaseCommand, CommandError
from django.utils import translation
from django.contrib.auth import get_user_model

from honey.models import Project, ProjectCommit

from gittle import Gittle

class Command(BaseCommand):
    help = 'Grabs the latest commits for a project and creates relevant buzzes \
            when found.'

    def handle(self, *args, **options):
        projects = Project.objects.all()

        for project in projects:
            print('Checking {0} for new commits'.format(project))
            if project.git_url:
                repo_path = '/tmp/' + project.slug
                try:
                    repo = Gittle(repo_path, project.git_url)
                    repo.pull()
                except:
                    try:
                        repo = Gittle.clone(project.git_url, repo_path)
                    except:
                        # put some logging here
                        repo = None
                if repo:
                    new_commits = []
                    for commit in repo.commit_info():
                        try:
                            prev_commit = repo.get_previous_commit(commit['sha'])
                            time = (datetime.fromtimestamp(commit['time']) + timedelta(hours=commit['timezone']/(60*60))).replace(tzinfo=pytz.utc)
                            try:
                                user_author = get_user_model().objects.get(email=commit['author']['email'])
                                string_author = None
                            except:
                                string_author = commit['author']['name']
                                user_author = None

                            summary = commit['message'].split('\n')[0][:45]
                            pcommit = ProjectCommit.objects.create(
                                project=project,
                                chash=commit['sha'],
                                message=commit['message'],
                                summary=summary,
                                user_author=user_author,
                                string_author=string_author,
                                created=time,
                                time=time,
                                diff=repo.diff(commit['sha'], prev_commit).next()['diff']
                            )
                            print(pcommit, ' added.')
                            new_commits.append(pcommit)
                        except:
                            pass