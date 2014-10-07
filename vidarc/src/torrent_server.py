import libtorrent as lt

DEFAULT_PORTS = (6881, 6891)


class TorrentServer:

    handlers = {}

    def __init__(self, app, db=None):
        self.sess = lt.session()
        min_port, max_port = DEFAULT_PORTS
        if 'TORRENT_PORTS' in app.config:
            min_port, max_port = app.config['TORRENT_PORTS']
        self.sess.listen_on(min_port, max_port)

        if db:
            self._load_from_db(db)

    def _load_from_db(self, db):
        pass

    def add(self, torrent_path, file_path):
        if torrent_path in self.handlers:
            return
        info = lt.torrent_info(torrent_path)
        h = self.sess.add_torrent({'ti': info, 'save_path': file_path})
        self.handlers[torrent_path] = h

    def remove(self, torrent_path):
        if torrent_path in self.handlers:
            self.sess.remove_torrent(self.handlers[torrent_path])