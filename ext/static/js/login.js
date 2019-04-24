$(document).ready(function () {
    $("#login").click(function () {
        $.post("login", {
            _xsrf: $("input[name='_xsrf']").val(),
            username: $("input[name='username']").val(),
            password: $("input[name='password']").val(),
            remember: $("input[name='remember']").val()
        },
            function (data, state) {
                if (data["errors"] == "Success") {
                    var prevUrl = document.referrer;
                    if (prevUrl == '' || /.*\/login.*/.test(prevUrl) || /.*\/register.*/.test(prevUrl) || /.*\/reset-password.*/.test(prevUrl)) {
                        prevUrl = '/';
                    };
                    window.location.href = prevUrl;
                } else {
                    htmlcode = ["<div class=\"alert alert-warning alert-dismissible\" role=\"alert\">",
                        "<button type=\"button\" class=\"close\" data-dismiss=\"alert\" aria-label=\"Close\">",
                        "<span aria-hidden=\"true\">&times;</span></button>",
                        "<strong>Warning!</strong> ",
                        "<p>Wrong username or password.</p>",
                        "</div>"].join("");
                    $("#loginhint").html(htmlcode);
                }
                return true;
            });
    });
});