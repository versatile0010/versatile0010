## update_blogPost.py
import feedparser

blog_url = "https://versatile0010.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 5

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx > MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """

# Jaehyeon Lee
- **Backend Engineer**

![mejwh](https://github.com/versatile0010/versatile0010/assets/96612168/afd44276-3b69-40df-a520-d981feabcb17)



📚 **tech stack**
```sql
- language
  - Java

- framework
  - Spring Boot

- database
  - RDBMS
      - MySQL
      - MariaDB
  - NoSQL
      - Redis

- infra
  - AWS, docker, jib, github actions, jenkins

- cowork
  - jira, confluence, slack, notion, figma
```

📞  **contact**
```yml
woguns@gmail.com
```

"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
