$(function () {
    var $username = $("#username_input");
    $username.change(function () {


        var username = $username.val().trim();
        if (username.length) {
            $.getJSON('staff_user/checkuser/', {'username': username}, function (data) {
                console.log(data);
            })

        }
    })
})