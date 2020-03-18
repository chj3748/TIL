$('#pwc').keyup(function () {
    var pwd1 = $("#pw").val();
    var pwd2 = $("#pwc").val();
    if ( pwd1 != '' && pwd2 == '' ) {
        $("#pwc+p").text("동일하게 입력 해주세요.");
        $("#pwc+p").css('color','gray');
    } else if (pwd1 != "" || pwd2 != "") {
        if (pwd1 == pwd2) {
            $("#pwc+p").text("비밀번호가 일치합니다.");
            $("#pwc+p").css('color', 'green');
        } else {
            $("#pwc+p").text("비밀번호가 일치하지 않습니다.");
            $("#pwc+p").css('color', 'red');
        }
    }
});
