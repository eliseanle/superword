$('#show-definition').click(function(){
    $('#definition-container').fadeIn();
});

$('#show-hide').click(function(){
    var hideText = '&nbsp; Hide';
    var showText = '&nbsp; Show';
    var isHidden = $(this).html() == hideText;
    if (isHidden){
        $(this).html(showText);
        $('#open-close').attr('class','glyphicon glyphicon-eye-open');
        $('#words_display').fadeOut();
    } else {
        $(this).html(hideText);
        $('#open-close').attr('class','glyphicon glyphicon-eye-close');
        $('#words_display').fadeIn();

    }
});

$('.delete-word').click(function(){
    var container = $(this);
    var theWord = container.attr('name');
    $.ajax({
        type: 'POST',
        url: '/add/delete_word/',
        dataType : 'json',
        data: {'word': theWord},
        success: function(response) {
            container.parent().parent().remove();
        },
        error: function() {alert('SERVER FAILURE')}
      });
});