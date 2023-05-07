## elasticsearch v7.17.0 docker image
`docker pull docker.elastic.co/elasticsearch/elasticsearch:7.17.10`

## start elasticsearch docker image v 7.17.0
`docker run -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.17.10`
