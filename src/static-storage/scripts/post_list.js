function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}


$(document).ready(function () {
    
    var query = getParameterByName('q')
    var postList = [];
    var nextPostUrl;

    function attachPost(postValue, prepend) {
        var postContent = postValue.content;
        var postUser = postValue.user;
        var timeSince = postValue.timesince;
        var postHtmlBody = '<div class="card card-small card-post mb-4" >'+
            '<div class="card-body" >'+
                '<div class="card-post__author d-flex">'+
                    '<a href="#" class="card-post__author-avatar card-post__author-avatar--small" style="background-image: url(\'images/avatars/1.jpg\');">Written by James Khan</a>'+
                    '<div class="d-flex flex-column justify-content-center ml-3">'+
                        '<span class="card-post__author-name">' + '<a href="'+ postUser.url +'">@' + postUser.username + '</a></span>'+
                        '<small class="text-muted">'+ timeSince +'</small>'+
                    '</div>'+
                '</div> <hr>'+
                    '<!-- <h5 class="card-title">{{ object.title }}</h5> -->'+
'<p class="card-text text-muted">' + postContent + '</p>'+
        '</div>'+
                '<div class="card-footer border-top d-flex">'+
                    '<div class="my-auto ml-2">'+
                        '<a class="btn btn-sm btn-white" href="#"> Like <span class="badge badge-pill badge-primary">22323</span></a>'+
                    '</div>'+
                    '<div class="my-auto ml-2">'+
                        '<a class="btn btn-sm btn-white" href="#"> Dislike <span class="badge badge-pill badge-danger">22323</span> </a>'+
                    '</div>'+
                    '<div class="my-auto ml-2">'+
                        '<a class="btn btn-sm btn-white" href="#"> Share <span class="badge badge-pill badge-success">22323</span> </a>'+
                    '</div>'+
                    '<div class="my-auto ml-auto">'+
                        '<a class="btn btn-sm btn-white" href="#"> Read more </a>'+
                    '</div>'+
                '</div>'+
                '</div>';
        if(prepend == true){
            $("#post-list").prepend(postHtmlBody);
        }else{
            $("#post-list").append(postHtmlBody);
        }
    }

    function parsePosts() {
        if(postList == 0){
            $("#post-list").text("No Posts Found!")
        }else{
            $.each(postList, function (key, value) {
                var postKey = key;
                attachPost(value,false)
            })
        }

    }

    function fetchPosts(url) {
        console.log('fetching...')
        var fetchUrl;
        if(!url){
            fetchUrl = '/api/post/';
        }else{
            fetchUrl = url
        }
        $.ajax({
            url: fetchUrl,
            method: 'GET',
            data: {
                'q':query
            },
            success: function (data) {
                postList = data.results
                if(data.next){
                    nextPostUrl = data.next
                }else{
                    $('#loadmore').css("display","none")
                }
                
                parsePosts()
            },
            error: function (data) {
                console.log("error")
                console.log(data)
            }    
        })
    }
    fetchPosts()

    $('#loadmore').click(function(event){
        event.preventDefault()
        if(nextPostUrl){
            fetchPosts(nextPostUrl)
        }
    })

    $("#post-form").submit(function(event){
        event.preventDefault()
        var this_ = $(this) 
        var formData = this_.serialize()

        $.ajax({
            url: '/api/post/create/',
            method: 'POST',
            data: formData,
            success: function (data) {
                attachPost(data,true);
                this_.find("input[type=text], textarea").val("")
            },
            error: function (data) {
                console.log("error")
                console.log(data)
            }
        })
    })
});
