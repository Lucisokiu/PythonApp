import kivy
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.filechooser import FileChooserListView
from kivy.uix.screenmanager import Screen
from kivy.uix.widget import Widget
from kivy.uix.camera import Camera
import cv2
import tkinter as tk
from tkinter import filedialog

from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.filemanager import MDFileManager

class StartButton(Widget):
    def take_picture_from_camera(self):
        # khởi tạo đối tượng VideoCapture để mở máy ảnh trên điện thoại di động
        cap = cv2.VideoCapture(0)

        # kiểm tra xem máy ảnh đã mở thành công chưa
        if not cap.isOpened():
            print("Không thể mở máy ảnh")
            exit()

        # đọc từng khung hình từ máy ảnh và hiển thị lên màn hình
        while True:
            ret, frame = cap.read()

            if not ret:
                print("Không thể đọc khung hình từ máy ảnh")
                break

            # hiển thị khung hình lên màn hình
            cv2.imshow("Camera", frame)

            # chờ 1ms để xem nếu người dùng nhấn phím 'q' để thoát
            key = cv2.waitKey(1)
            if key == ord("q"):
                break
            elif key == ord("c"):
                # chụp hình và lưu vào file
                self.camera.export_to_png("picture/captured_image.jpg", frame)
                print("Đã lưu ảnh")

        # giải phóng tài nguyên
        cap.release()
        cv2.destroyAllWindows()
    # def take_picture_from_libary(self):
    #     dialog = None
    #     file_manager = None
    #     file_path = StringProperty('')
    #     self.file_manager.show('/') # show thư mục gốc
    #
    #     def select_path(self, path):
    #         self.file_path = path
    #         self.exit_file_manager()
    #
    #     def exit_file_manager(self, *args):
    #         self.file_manager.close()
    #         self.dialog = MDDialog(
    #             title='Đã chọn ảnh',
    #             text=self.file_path,
    #             buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)]
    #         )
    #         self.dialog.open()
    #
    #     def close_dialog(self, *args):
    #         self.dialog.dismiss()


class MainApp(MDApp):
    dialog = None
    file_manager = None
    file_path = kivy.properties.StringProperty('')

    def show_file_manager(self):
        self.file_manager = MDFileManager(
            exit_manager=self.exit_file_manager,
            select_path=self.select_path,
            preview=True,
        )
        self.file_manager.show('/')  # show thư mục gốc

    def select_path(self, path):
        self.file_path = path
        self.exit_file_manager()

    def exit_file_manager(self, *args):
        self.file_manager.close()
        self.dialog = MDDialog(
            title='Đã chọn ảnh',
            text=self.file_path,
            buttons=[MDFlatButton(text='OK', on_release=self.close_dialog)]
        )
        self.dialog.open()

    def close_dialog(self, *args):
        self.dialog.dismiss()


class StartScreen(App):
    pass

class MainWidget(Widget):
    pass

class ImageProcessing(App):
    pass




if __name__ == '__main__':
    # StartScreen().run()
    # ImageProcessing().run()
    MainApp().run()
