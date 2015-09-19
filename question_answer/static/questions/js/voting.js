$(document).ready(function() {
    $(".upvote").click(function() {
        var score = +$(this).next("h4").text();
        $(this).next("h4").text(++score);
        var p = $(this).parents("div[id*='answer']");
        if (p.length > 0) {
            var id = p.attr('id');
            id = id.split("-")[1];
            //alert("/answer/up/"+id);
            $.get("/questions/answer/"+id+"/up/", function(){});
        }
        else {
            $.get("up/", function(){});
        }
    });

    $(".downvote").click(function() {
        // this should use #downvote but onlly upvote works.
        // so that's the way it stays
        var score = +$(this).siblings("h4").text();
        if (score > 0) {
            $(this).siblings("h4").text(--score);
        }
        var p = $(this).parents("div[id*='answer']");
        if (p.length > 0) {
            var id = p.attr('id');
            id = id.split("-")[1];
            //alert("/answer/up/"+id);
            $.get("/questions/answer/"+id+"/down/", function(){});
        }
        else {
            $.get("down/", function(){});
        }

    });

});
