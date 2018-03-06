class Util {
    static encode(data) {
        return Object.entries(data).map(([key, val]) => `${key}=${val}`).join('&');
    }

    static getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
}


class Main {
    constructor(data) {
        this.data = data;
    }

    get_comments() {

        var user_id = this.data.user_id;
        var like_url = this.data.routes.static_urls.like;

        $('#comments_loader').show();

        $.ajax({
            type: 'get',
            url: this.data.routes.comments_get,

            success: (html) => {

                var comments = html.comments;
                var comments_count = html.comments_count;
                html = "";

                $.each(comments, function (index, value) {

                    html += value.pub_date + "&nbsp;&nbsp;&nbsp;" +
                        "<a class='comments_link' href=''><img id='" + value.id + "' height='17px;' src=" +
                        like_url + "></a>" + "&nbsp;";

                    if (value.is_liked == 1) {
                        html += "<span style='color: #cc0000;'>" + value.count_likes + "</span>";
                    }
                    else {
                        html += "<span>" + value.count_likes + "</span>";
                    }
                    if (value.user_id == user_id)
                    {
                        html += "&nbsp;&nbsp;&nbsp;<button onclick='main.edit_comment(" + value.id + ")'>Редактировать" +
                        "</button>&nbsp;&nbsp;&nbsp;<button onclick='main.delete_comment(" + value.id + ")'>Удалить</button>";
                    }
                    html += "<br><b>" + value.username + ":</b><br>&nbsp;&nbsp;&nbsp;" + value.content + "<br><br>";
                });

                $('#content').val('');
                $('#comments').html(html);
                $('#count_comments').html(comments_count + " comments");
                $('#comments_loader').hide();

                let $links = document.querySelectorAll('.comments_link');

                $links.forEach(($link) => {

                    $link.addEventListener('click', (e) => {
                    e.preventDefault();
                    this.add_like_comment(e.target);
            });})
            }
        });
    }

    get_likes() {

        $('#likes_loader').show();

        $.ajax({
            type: 'get',
            url: this.data.routes.likes_get,

            success: function (html) {
                $('#count_likes').html(html.count_likes);

                if (html.is_liked == true) {
                    $('#is_liked').html('Вам понравилось.<br><br>');
                }

                else {
                    $('#is_liked').html('');
                }

                $('#likes_loader').hide();
            }
        });
    }

    add_like_article() {

        var like_data = Util.encode({
            'article': this.data.article_id,
            'csrfmiddlewaretoken': this.data.csrf_token});

        $.ajax({
            type: 'post',
            url: this.data.routes.article_like,
            data: like_data,

            success: (html) => {
                this.get_likes();
            },

            error: function() {
                alert('Server-side error!');
            }
        });
    }

    add_like_comment(a) {

        data = Util.encode({'comment': a.getAttribute('id'),
                       'csrfmiddlewaretoken': this.data.csrf_token});

        $.ajax({
            type: 'post',
            url: this.data.routes.comment_like,
            data: data,

            success: (html) => {
                this.get_comments();
            },

            error: function () {
                alert('Server-side error!');
            }
        });
    }

    add_comment() {

        var form = $('#add_comment_form').serialize();

        $.ajax({
            type: 'post',
            url: this.data.routes.comment_add,
            data: form,
            success: (html) => {
                this.get_comments();
            },
            error: function () {
                alert('Server-side error!');
            }
        });
    }

    edit_comment(id) {
        window.location.href = '/blog/comments/' + id + '/edit';
    }

    delete_comment(id) {

        data = Util.encode({'id': id, 'csrfmiddlewaretoken': this.data.csrf_token});

        $.ajax({
            type: 'post',
            url: this.data.routes.comment_delete,
            data: data,
            success: (html) => {
                this.get_comments();
            },
            error: function () {
                alert('Server-Side error!');
            }
        });
    }
}