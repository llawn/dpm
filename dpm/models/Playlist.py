class Playlist:
    def __init__(
        self,
        playlist_id,
        playlist_name,
        playlist_created_at,
        playlist_created_by,
        playlist_last_modified,
    ):
        self.playlist_id = playlist_id
        self.playlist_name = playlist_name
        self.playlist_created_at = playlist_created_at
        self.playlist_created_by = playlist_created_by
        self.playlist_last_modified = playlist_last_modified

    def to_dict(self):
        dict = {
            "playlist_id": self.playlist_id,
            "playlist_name": self.playlist_name,
            "playlist_created_at": self.playlist_created_at,
            "playlist_created_by": self.playlist_created_by,
            "playlist_last_modified": self.playlist_last_modified,
        }
        return dict
