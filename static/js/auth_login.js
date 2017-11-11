$(document).ready(function(){

	$("#btnLogin").click(function(){
		
		 $.ajax({
            url: '/loadMain',
            data: $('.form-login').serialize(),
            type: 'POST',
            success: function(response) {
                console.log(response);
            },
            error: function(error) {
                console.log(error);
            }
        });
	});
});