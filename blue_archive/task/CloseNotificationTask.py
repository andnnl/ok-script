from typing_extensions import override

from autoui.task.FindFeatureTask import FindFindFeatureTask
from blue_archive.scene.NotificationScence import NotificationScene


class CloseNotificationTask(FindFindFeatureTask):

    @override
    def run_frame(self):
        if self.is_scene(NotificationScene):
            print(f"Start scene click")
            self.click_box(self.scene.close_event, 0.85)
            self.sleep(1)
