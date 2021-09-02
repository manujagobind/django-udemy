from datetime import date

from django.shortcuts import render


all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Gobind",
        "date": date(2021, 9, 2),
        "title": "Mountain Hiking",
        "excerpt": """There's nothing like the views you get when hiking in the 
                    mountains! And I wasn't even prepared for what happened whilst i
                    was enjoying the view!""",
        "content": """
            Dolorum laboriosam doloremque recusandae eveniet saepe, unde reprehenderit
            aspernatur esse qui quaerat? Amet aliquam veniam accusamus? Optio debitis 
            itaque voluptatibus enim quas aut, cum sed architecto commodi perferendis enim accusamus 
            ad similique, saepe labore earum repudiandae ab assumenda? Totam quo ratione aperiam corrupti, 
            perspiciatis officia eum voluptatum, in atque rerum molestiae tenetur error sapiente fugit repellat 
            voluptatum adipisci? Officia quaerat molestias aut consequuntur nulla mollitia aliquam deleniti.

            Dolorum laboriosam doloremque recusandae eveniet saepe, unde reprehenderit
            aspernatur esse qui quaerat? Amet aliquam veniam accusamus? Optio debitis 
            itaque voluptatibus enim quas aut, cum sed architecto commodi perferendis enim accusamus 
            ad similique, saepe labore earum repudiandae ab assumenda? Totam quo ratione aperiam corrupti, 
            perspiciatis officia eum voluptatum, in atque rerum molestiae tenetur error sapiente fugit repellat 
            voluptatum adipisci? Officia quaerat molestias aut consequuntur nulla mollitia aliquam deleniti.

            Dolorum laboriosam doloremque recusandae eveniet saepe, unde reprehenderit
            aspernatur esse qui quaerat? Amet aliquam veniam accusamus? Optio debitis 
            itaque voluptatibus enim quas aut, cum sed architecto commodi perferendis enim accusamus 
            ad similique, saepe labore earum repudiandae ab assumenda? Totam quo ratione aperiam corrupti, 
            perspiciatis officia eum voluptatum, in atque rerum molestiae tenetur error sapiente fugit repellat 
            voluptatum adipisci? Officia quaerat molestias aut consequuntur nulla mollitia aliquam deleniti.
        """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Maximilian",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Maximilian",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
]


def get_date(post):
    return post.get('date')


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        'posts': latest_posts
    })


def posts(request):
    return render(request, "blog/all-posts.html", {
        'posts': all_posts
    })


def post_detail(request, slug):
    post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        'post': post
    })
