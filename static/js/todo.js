$(document).ready(function(){
    var csrfToken = $("input[name=csrfmiddlewaretoken]")

    // Create Task
    $('#createButton').click(function(){
        var serializedData = $('#createTaskForm').serialize();
        $.ajax({
            url: $('#createTaskForm').data('url'),
            data: serializedData,
            type: 'post',
            success: function(response) {
                $('#taskList').append('<div class="card mb-1" id="taskCard" data-id="'+ response.task.id + '"><div class="card-body">'+ response.task.title +'<button type="button" class="btn-close float-right" data-id="'+ response.task.id + '" data-bs-dismiss="modal" aria-label="Close"></button></div></div>')
            }
        })
        $('#createTaskForm')[0].reset();
    })

    // Mark Task as Completed
    $('#taskList').on('click', '.card', function(){
        var dataId = $(this).data('id');
        $.ajax({
            url: dataId +'/completed/',
            data: {
                csrfmiddlewaretoken: csrfToken.val(),
                id: dataId
            },
            type: 'post',
            success: function(){
                var cardItem = $('#taskCard[data-id="'+ dataId+ '"]');
                cardItem.css('text-decoration', 'line-through').hide().slideDown();
                $('#taskList').append(cardItem);
            }
        })
    }).on('click', 'button-close', function(event){
        event.stopPropagation();
        var dataId = $(this).data('id');

        $.ajax({
            url: dataId +'/delete/',
            data: {
                csrfmiddlewaretoken: csrfToken.val(),
                id: dataId
            },
            type:'post',
            dataType: 'json',
            success: function(){
                $('#taskCard[data-id=" '+ dataId +' "]').remove();
            }
        })
    });
});
