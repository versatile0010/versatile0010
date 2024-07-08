## update_blogPost.py
import feedparser

blog_url = "https://versatile0010.github.io/feed.xml"
rss_feed = feedparser.parse(blog_url)

MAX_NUM = 3 

latest_posts = ""

for idx, entrie in enumerate(rss_feed['entries']):
  if idx >= MAX_NUM:
     break;
  feed_date = entrie['published_parsed']
  latest_posts += f" - [{feed_date.tm_mon}/{feed_date.tm_mday} - {entrie['title']}]({entrie['link']})\n"

preREADME = """

# Jaehyeon Lee
- **Backend Engineer**

📚 **tech stack**
```sql
 Java, Kotlin, Spring, JPA, Querydsl, MariaDB, Redis, Git, AWS, Docker, Jenkins, Junit5
```

📞  **contact**
```yml
woguns@gmail.com
```

---
📝 **Latest Blog posts**

"""

resultREADME = f"{preREADME}{latest_posts}"

with open("README.md", "w", encoding='utf-8') as f :
  f.write(resultREADME)
