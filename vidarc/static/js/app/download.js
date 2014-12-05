define(['app/longPolling'], function(LongPolling) {
    function FreshBox(options) {
        this.downloadItems = [];
        this.url = options.url;
        this.itemTemplate = options.itemTemplate;

        this.widget = options.downloadWidget;
        this.downloadList = this.widget.querySelector("#download-list");
        this.downloadForm = this.widget
        this.errorsDiv = this.downloadForm.querySelector(".download-errors");

        this.lp = new LongPolling(this.url);
        this.lp.on("addItem", this.onAddItem.bind(this));
        this.lp.on("delItem", this.onDelItem.bind(this));
        this.lp.start();
    }

    FreshBox.prototype.onAddItem = function(e) {
        var div = this.downloadItems[e.id];
        if (!div) {
            div = document.createElement("div");
            this.downloadList.appendChild(div);
        }
        div.innerHTML = this.itemTemplate({'type': e.id, 'title': e.title});

        this.downloadItems[e.id] = div;
    };


    FreshBox.prototype.onDelItem = function(e) {

    };

    return FreshBox;
});