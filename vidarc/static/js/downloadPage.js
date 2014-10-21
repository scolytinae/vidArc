require(['common', 'app/download'], function(common, FreshBox){
    var options = {
        'elem': document.body,
        'url': 'api/downloads'
    };

    new FreshBox(options);
});

