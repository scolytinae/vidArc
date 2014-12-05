define(['app/eventMixin'], function(eventMixin) {
    function LongPolling(url) {
        for(var method in eventMixin) {
            this[method] = eventMixin[method];
        }
        this.url = url;

        this.xhr = new XMLHttpRequest();
        this.xhr.onreadystatechange = this.onReadyStateChange.bind(this);
    }

    LongPolling.prototype.start = function() {
        this.xhr.open('GET', this.url + '?type=full', true);
        this.xhr.send();
    };

    LongPolling.prototype.onReadyStateChange = function() {
        if (this.xhr.readyState != 4) return;

        if (this.xhr.status != 200) {
            console.log(this.xhr.status + ': ' + this.xhr.statusText);
        } else {
            var rsv = JSON.parse(this.xhr.responseText);
            this.processItems(rsv.data);
        }

        this.xhr.open('GET', this.url, true);
        this.xhr.send();
    };

    LongPolling.prototype.processItems = function(items) {
        for (var i = 0; i < items.length; ++i) {
            var item = items[i];
            switch (item.state) {
                case 'active':
                    this.trigger('addItem', item);
                    break;
                case 'done':
                    this.trigger("doneItem", item);
                    break;
                case 'pause':
                    this.trigger("pauseItem", item);
                    break;
                case 'delete':
                    this.trigger("delItem", item);
                    break;
                case 'error':
                    this.trigger("error", item);
                    break;
            }
        }
    };

    return LongPolling;
});
