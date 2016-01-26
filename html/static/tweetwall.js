$(document).ready(function () {

    var ws;
    var url = "ws://localhost:8999";

    ws = new WebSocket(url);
    var channels = [];
    ws.onmessage = function (evt) {

        var tweet = JSON.parse(evt.data);
        console.log(tweet);
        var tweet_html = "<div class=\"tweet\" >" +
            "<p><span class=\"names\"><img class=\"profile_img\" src=\"" +
            tweet.user.profile_image_url + "\" />" +
            "<span class=\"username\">" + tweet.user.name + "</span>" +
            "<span class=\"nickname\">(" + tweet.user.screen_name + ")</span></p>" +
            "<p >" + tweet.text + "</p>";
        if (tweet.entities.media != undefined) {
            tweet_html = tweet_html + "<p align=center><img width=95% src=\"" + tweet.entities.media[0].media_url + "\"/></p>";
        }
        tweet_html = tweet_html + "<p><span class=\"timestamp\">" + tweet.created_at + "</span></p>" +
            "</div>";

        var channel = tweet.channel.replace(/[, ]/g, "_");
        if ($.inArray(channel, channels) == -1) {
            channels.push(channel);
            var wallstrip = "<td class=\"wallstrip\" id=\"" + channel + "\"></td>";
            var walltitle = "<td class=\"walltitle\">" + tweet.channel.replace(/,/g, " ") + "</td>";
            $(walltitle).appendTo($("#walltitles"));
            $(wallstrip).appendTo($("#wall"));
        }

        $(tweet_html).hide().prependTo($("#" + channel)).slideDown(300);
    };
    ws.onclose = function (evt) {
        alert("Connection close");
    };
    ws.onopen = function (evt) {
        $("#connection_icon").addClass("connected").removeClass("disconnected");
    };

});
