function getCookie(name) 
{
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

$(document).on('click', '.like', function()
{
    var id = $(this).data('id');
    $.ajax({
        url : "like/",
        type : "POST",
        data : { id : id },
        dataType: 'json',
        success : function(response) 
        {
            if (response.status == 'success')
            {
                $('.nbrLike'+id).html(response.like);
            }
        },
        error : function(xhr,errmsg,err) 
        {
            console.log(xhr.status + ": " + xhr.responseText);
        }
    });

});