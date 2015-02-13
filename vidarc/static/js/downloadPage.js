require(['common', 'lib/lodash', 'app/download'], function(common, _, FreshBox){
    var options = {
        'url': 'api/downloads',
        'downloadWidget': document.querySelector('#download-widget'),
        'itemTemplate': _.template(document.querySelector('#download-list-item').innerHTML),
        'errorTemplate': _.template(document.querySelector('#download-errors-item').innerHTML)
    };

    new FreshBox(options);
});

