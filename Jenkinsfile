properties([[$class: 'JiraProjectProperty'], pipelineTriggers([cron('H/2 * * * *'), pollSCM(ignorePostCommitHooks: true, scmpoll_spec: 'H/2 * * * *')])])
node{
 stage("1")
 git credentialsId: 'c8238df7-eca5-48ea-a075-eb5aa5ec78dc', url: 'https://github.com/ofirshi/WorldOfGames.git'
 sh "ls"
}
