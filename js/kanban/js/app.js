var Kanban = { };

Kanban.init = function (container) {
    var colorBlock, state;
    this.container = container;
    $('#priority-forms').children('button').click(function () {
        $('#priority-forms').attr('select-color', $(this).css('background-color'));
    });

    var flagmarkClick = function (e) {
        e.stopImmediatePropagation();
        Kanban.selectedItem = $(this);
        showCommentDialog();
    };

    var showCommentDialog = function () {
        $('#commentInput').val(Kanban.selectedItem.attr('title'));
        $('#add-comment-forms').css('visibility', 'visible').dialog({
            width: '500px',
            buttons: {
                'Save': function() {
                    Kanban.selectedItem.attr('title', $('#commentInput').val());
                    Kanban.selectedItem.css('background-color', $('#priority-forms').attr('select-color'));

                    $(this).dialog("close");
                    $('#commentInput').val('');
                    Kanban.selectedItem = null;
                    Kanban.saveStateToLocalStorage();
                },
                'Cancel': function() {
                    $('#commentInput').val('');
                    $(this).dialog( "close" );
                    Kanban.selectedItem = null;
                }
            }});
    };

    state = window.localStorage.getItem('core-assembly-classes');
    if (state) {
        classList = JSON.parse(state);
    }

    for (var key in classList) {
        if(!classList.hasOwnProperty(key)) continue;

        var name, content, classes, columnDiv;

        name = classList[key].name;
        classes = classList[key].classes;
        columnDiv = $('<div />').addClass('col-md-2');
        columnDiv.append($('<li />').addClass('list-group-item').append($('<h3 />').html(name)));
        content = $('<div />').addClass('connectedSortable');
        columnDiv.append(content);

        for (var i = 0; i < classes.length; i++) {
            var li = $('<li />').addClass('list-group-item').html(this.trunkText(classes[i].n, 23)).attr('title', classes[i].n);
            var flagmark = $('<span>&nbsp;</span>').addClass('flagmark').click(flagmarkClick);
            if(classes[i].bg) {
                flagmark.css('background-color', classes[i].bg);
            }

            flagmark.attr('title', classes[i].cmt ? classes[i].cmt :  '');

            li.append(flagmark);
            content.append(li);
        }

        container.append(columnDiv);
    }
};

Kanban.trunkText = function (str, length) {
    if (str.length > length) {
        str = str.substr(0, length) + '...';
    }

    return str;
};

Kanban.getStateToSave = function (container) {
    var treeState = [];

    var columnDivs = container.children();
    for (var i = 0; i < columnDivs.length; i++) {
        var columnDiv = $(columnDivs[i]);
        var header = columnDiv.children('.list-group-item').text();
        var content = columnDiv.children('.connectedSortable');

        var columnObj = {};
        columnObj.name = header;
        columnObj.classes = [];
        var lis = content.children('li');
        for (var j = 0; j < lis.length; j++) {
            var li = $(lis[j]);
            var className = li.text();
            var classInfo = {'n':className};

            var bgColor = li.children('span').css('background-color');
            if(bgColor != 'rgba(0, 0, 0, 0)') {
                classInfo.bg = bgColor;
            }

            var comment = li.children('span').attr('title');
            if(comment) {
                classInfo.cmt = comment;
            }

            columnObj.classes.push(classInfo);
        }

        treeState.push(columnObj);
    }

    return JSON.stringify(treeState);
};

Kanban.saveStateToLocalStorage = function() {
    var state = this.getStateToSave(this.container);
    localStorage.setItem('core-assembly-classes', state);
};


