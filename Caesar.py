import customtkinter as ctk
import sys

class CaesarCipher(ctk.CTk):
    
    def __init__(self):
        super().__init__()
        
        self.title('Caesar Cipher')
        self.geometry('800x500')
        self.resizable(False, False)

        self.letters = 'abcdefghijklmnopqrstuvwxyz'
        self.num_letters = len(self.letters)

        # Configure Appearance Mode
        ctk.set_appearance_mode("Dark")  # Options: "Dark", "Light", "System"
        ctk.set_default_color_theme("green")  # Available themes: "blue", "green", "dark-blue"

        # Main Frame
        self.main_frame = ctk.CTkFrame(self, corner_radius=10, fg_color="#252626")
        self.main_frame.pack(fill="both", expand=True, padx=30, pady=30)

        # Title Label
        self.title_label = ctk.CTkLabel(
            self.main_frame,
            text="Caesar Cipher",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="#D1E8E2"
        )
        self.title_label.pack(pady=(10, 20))

        # Textbox for Input/Output
        self.text_box = ctk.CTkTextbox(
            self.main_frame,
            height=150,
            width=500,
            font=ctk.CTkFont(size=16),
            border_width=1,
            border_color="#8EAF9D"
        )
        self.text_box.pack(pady=(10, 20), padx=20)

        # Key Input and Buttons
        self.control_frame = ctk.CTkFrame(self.main_frame, corner_radius=10)
        self.control_frame.pack(fill="x", pady=10, padx=20)

        self.key_label = ctk.CTkLabel(
            self.control_frame,
            text="Key (1-25):",
            font=ctk.CTkFont(size=16),
            text_color="#A8D5BA"
        )
        self.key_label.grid(row=0, column=0, padx=15, pady=15)

        # Key Entry Validation Command
        self.key_validation_command = self.register(self.validate_key)
        self.key_entry = ctk.CTkEntry(
            self.control_frame,
            width=70,
            font=ctk.CTkFont(size=16),
            justify="center",
            border_width=1,
            fg_color="#252626",
            border_color="#8EAF9D",
            validate="key",
            validatecommand=(self.key_validation_command, '%P')
        )
        self.key_entry.grid(row=0, column=2, padx=15, pady=15)

        self.encrypt_button = ctk.CTkButton(
            self.control_frame,
            text="Encrypt",
            command=self.encrypt_command,
            font=ctk.CTkFont(size=16),
            fg_color="#4A7C59",
            hover_color="#36694A",
            state="disabled"  # Initially disabled
        )
        self.encrypt_button.grid(row=0, column=3, padx=15, pady=15)

        self.decrypt_button = ctk.CTkButton(
            self.control_frame,
            text="Decrypt",
            command=self.decrypt_command,
            font=ctk.CTkFont(size=16),
            fg_color="#4A7C59",
            hover_color="#36694A",
            state="disabled"  # Initially disabled
        )
        self.decrypt_button.grid(row=0, column=4, padx=15, pady=15)

    def validate_key(self, value):
        """Validate key entry and enable/disable buttons."""
        if value == "":
            self.encrypt_button.configure(state="disabled")
            self.decrypt_button.configure(state="disabled")
            return True
        if value.isdigit():
            key = int(value)
            if 1 <= key < self.num_letters:
                self.encrypt_button.configure(state="normal")
                self.decrypt_button.configure(state="normal")
                return True
        self.encrypt_button.configure(state="disabled")
        self.decrypt_button.configure(state="disabled")
        return False

    def encrypt_decrypt(self, text, mode, key):
        result = ""
        if mode == 'd':
            key = -key

        for letter in text:
            letter = letter.lower()
            if letter == ' ':
                result += letter
                continue
            index = self.letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = (index + key) % self.num_letters
                result += self.letters[new_index]
        return result

    def encrypt_command(self):
        key = int(self.key_entry.get())
        text = self.text_box.get("1.0", "end").strip()
        encrypted_text = self.encrypt_decrypt(text, 'e', key)
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", encrypted_text)

    def decrypt_command(self):
        key = int(self.key_entry.get())
        text = self.text_box.get("1.0", "end").strip()
        decrypted_text = self.encrypt_decrypt(text, 'd', key)
        self.text_box.delete("1.0", "end")
        self.text_box.insert("1.0", decrypted_text)


if __name__ == "__main__":
    app = CaesarCipher()
    app.mainloop()
