from __future__ import annotations


class YouTubeUploaderFacade:
  def __init__(self, client_id, client_secret) -> None:
    self._file_manager = FileManager()
    self._video_converter = VideoConverter()
    self._youtube_api = YouTubeAPI()
    self._client_id = client_id
    self._client_secret = client_secret

  def upload(self, file_path) -> None:
    data = self._file_manager.read_from_disc(file_path)
    video = self._video_converter.convert(data, file_path, "mp4")
    self._youtube_api.upload(video, self._client_id, self._client_secret)


class FileManager:
  def read_from_disc(self, file_path: str) -> bytearray:
    pass


class YouTubeAPI:
  def upload(self, video: Video, client_id: str, client_secret: str) -> None:
    pass


class VideoConverter:
  def convert(self, data: bytearray, file_path: str, format: str) -> Video:
    pass


class Video:
  def __init__(self, name: str, format: str, data: bytearray) -> None:
    self.name = name
    self.format = format
    self.data = data


if __name__ == "__main__":
  youtube_uploader = YouTubeUploaderFacade(client_id="client-id", client_secret="client-secret")
  youtube_uploader.upload("D://Videos/video.mp4")
