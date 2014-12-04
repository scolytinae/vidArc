require(['common', 'lib/lodash', 'app/download'], function(common, _, FreshBox){
    var options = {
        'url': 'api/downloads',
        'downloadForm': document.querySelector('#download-form'),
        'downloadList': document.querySelector('#download-list'),
        'itemTemplate': _.template(document.querySelector('#download-list-item').innerHTML)
    };

    new FreshBox(options);
});

