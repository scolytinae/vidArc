define(function() {
    function FreshBox(options) {
        this.downloadItems = [];
        this.url = options.url;
        this.itemTemplate = options.itemTemplate;
        this.downloadList = options.downloadList;
        this.downloadForm = options.downloadForm;

        this.xhr = new XMLHttpRequest();

        this.getFullInfo();
    }

    FreshBox.prototype.getFullInfo = function() {
        this.xhr.open('GET', this.url + '?type=full', true);
        this.xhr.onreadystatechange = this.onReadyStateChange.bind(this);
        this.xhr.send();
    };

    FreshBox.prototype.addDownloadItem = function(item) {
        var div = document.createElement("div");
        div.innerHTML = this.itemTemplate({'type': item.id, 'title': item.title});
        this.downloadList.appendChild(div);

        this.downloadItems[item.id] = div;

        console.log(downloadItmes);
    };

    FreshBox.prototype.processDownloadItems = function(items) {
        for (var i = 0; i < items.length; ++i) {
            switch (items[i].cmd) {
                case 'add':
                    this.addDownloadItem(items[i]);
                    break;
                case 'del':
                    this.delDownloadItem(items[i]);
                    break;
            }
        }
    };

    FreshBox.prototype.delDownloadItem = function(info) {

    };

    FreshBox.prototype.onReadyStateChange = function() {
        if (this.xhr.readyState != 4) return;

        if (this.xhr.status != 200) {
            console.log(this.xhr.status + ': ' + this.xhr.statusText);
        } else {
            var rsv = JSON.parse(this.xhr.responseText);
            this.processDownloadItems(rsv.data);
            this.xhr.open('GET', this.url, true);
        }

        this.xhr.send();
    };

    return FreshBox;
});