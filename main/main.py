import os
import random
import string
import tkinter
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import DES_logic_func as des_logic
import AES_logic_func as aes_logic
import DES_key_gen_func as des_key


def get_decimal_value(binary_string):
    if binary_string == "00":
        return "0"
    elif binary_string == "01":
        return "1"
    elif binary_string == "10":
        return "2"
    elif binary_string == "11":
        return "3"
    elif binary_string == "0000":
        return "0"
    elif binary_string == "0001":
        return "1"
    elif binary_string == "0010":
        return "2"
    elif binary_string == "0100":
        return "4"
    elif binary_string == "1000":
        return "8"
    elif binary_string == "0011":
        return "3"
    elif binary_string == "0101":
        return "5"
    elif binary_string == "1001":
        return "9"
    elif binary_string == "0110":
        return "6"
    elif binary_string == "1010":
        return "10"
    elif binary_string == "1100":
        return "12"
    elif binary_string == "0111":
        return "7"
    elif binary_string == "1011":
        return "11"
    elif binary_string == "1101":
        return "13"
    elif binary_string == "1110":
        return "14"
    elif binary_string == "1111":
        return "15"


class TkinterApp(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        self.shared_data = {
            "plaintext": tkinter.StringVar(),
            "key": tkinter.StringVar(),
            "initial_permutation": tkinter.StringVar(),
            "right_side": tkinter.StringVar(),
            "changed_right_side": tkinter.StringVar(),
            "initial_left_side": tkinter.StringVar(),
            "decryption_right_side": tkinter.StringVar(),
            "decryption_changed_right_side": tkinter.StringVar(),
            "decryption_left_side": tkinter.StringVar(),
            "decryption_changed_left_side": tkinter.StringVar(),
            "AES_input": tkinter.StringVar(),
            "AES_key_1": tkinter.StringVar(),
            "AES_key_2": tkinter.StringVar(),
            "AES_plaintext_table": tkinter.StringVar(),
            "AES_key_1_table": tkinter.StringVar(),
            "AES_key_2_table": tkinter.StringVar(),
            "AES_ciphertext_table": tkinter.StringVar(),
            "Key_gen_original": tkinter.StringVar(),
            "Key_gen_Key": tkinter.StringVar(),
            "Key_gen_left": tkinter.StringVar(),
            "Key_gen_right": tkinter.StringVar()
        }

        container = Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        self.frames = {}

        for F in (Home_Page, DES_Page, DES_Image_Page, DES_Disclaimer_Page, DES_Encrypt_Page_1, DES_Encrypt_Page_2,
                  DES_Encrypt_Page_3, DES_Encrypt_Page_4, DES_Encrypt_Page_5, DES_Encrypt_Page_6, DES_Encrypt_Page_7,
                  DES_Encrypt_Page_8, DES_Decrypt_Page_1, DES_Decrypt_Page_2, DES_Decrypt_Page_3, DES_Decrypt_Page_4,
                  DES_Decrypt_Page_5, DES_Decrypt_Page_6, DES_Decrypt_Page_7, DES_Info_Page,
                  DES_Key_Gen_Page, DES_Key_Gen_Page_1, DES_Key_Gen_Page_2, DES_Key_Gen_Page_3, DES_Key_Gen_Page_4,
                  AES_Page, AES_Info_Page, AES_Image_Page, AES_Disclaimer_Page, AES_Encrypt_Page_1, AES_Encrypt_Page_2,
                  AES_Encrypt_Page_3, AES_Encrypt_Page_4, AES_Encrypt_Page_5, AES_Encrypt_Page_6, AES_Encrypt_Page_7,
                  AES_Decrypt_Page_1, AES_Decrypt_Page_2, AES_Decrypt_Page_3, AES_Decrypt_Page_4, AES_Decrypt_Page_5,
                  AES_Decrypt_Page_6, AES_Decrypt_Page_7):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("AES_Page")

    def show_frame(self, container):
        frame = self.frames[container]
        frame.updateText()
        frame.tkraise()


class Home_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        des_label = Label(self, text="Home", bg="#cf3030", font=("Arial", 25), fg="white")
        des_label.pack(fill='x', ipady=30)

        des_button = Button(self, text="DES", bg="#e88a1a", font=("Calibri", 25), fg="white",
                            command=lambda: controller.show_frame("DES_Info_Page"))
        des_button.pack(ipadx=200, ipady=50, expand=True)

        aes_button = Button(self, text="AES", bg="#e88a1a", font=("Calibri", 25), fg="white",
                            command=lambda: controller.show_frame("AES_Info_Page"))
        aes_button.pack(ipadx=200, ipady=50, expand=True)

    def updateText(self):
        pass


class DES_Info_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="DES", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        label_1_text = "\nThe Data Encryption Standard (DES) is a Symmetric Key Block Cipher created in 1976\n"
        label_1 = Label(self, text=label_1_text, font=("Calibri", 15), anchor='w')
        label_1.pack()

        input_text = "Inputs: 64-bit Plaintext and 64-bit Key (including 8 parity bits)"
        inputs_label = Label(self, text=input_text, font=("Calibri", 15), anchor='w')
        inputs_label.pack()

        output_text = "Output: 64-bit Ciphertext.\n"
        output_label = Label(self, text=output_text, font=("Calibri", 15), anchor='w')
        output_label.pack()

        label_2_text = "It is an implementation of a Feistel Network, meaning that reversing the steps taken to " \
                       "produce the output, the input can be found.\n"
        label_2 = Label(self, text=label_2_text, font=("Calibri", 15), anchor='w')
        label_2.pack()

        label_3_text = "The DES cipher is made up of an initial permutation, then 16 rounds of encryption through a " \
                       "Function and a final permutation.\n"
        label_3 = Label(self, text=label_3_text, font=("Calibri", 15), anchor='w')
        label_3.pack()

        label_4_text = "Each round is made up of 5 Steps:"
        label_4 = Label(self, text=label_4_text, font=("Calibri", 15), anchor='w')
        label_4.pack()

        step_1_text = "1. Expansion of the right side of the permuted text."
        step_1_label = Label(self, text=step_1_text, font=("Calibri", 15), anchor='w')
        step_1_label.pack()

        step_2_text = "2. XORing the expanded text with a 48-bit round key."
        step_2_label = Label(self, text=step_2_text, font=("Calibri", 15), anchor='w')
        step_2_label.pack()

        step_3_text = "3. Passing the right side into the S Box to shrink it down to 32-bits again."
        step_3_label = Label(self, text=step_3_text, font=("Calibri", 15), anchor='w')
        step_3_label.pack()

        step_4_text = "4. XORing the right side with the original permuted left side."
        step_4_label = Label(self, text=step_4_text, font=("Calibri", 15), anchor='w')
        step_4_label.pack()

        step_5_text = "5. The original permuted right side becomes the new left side and the new right " \
                      "side is the result of the XORing of the right side with the\n original permuted left side."
        step_5_label = Label(self, text=step_5_text, font=("Calibri", 15), anchor='w')
        step_5_label.pack()

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Image_Page"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

    def updateText(self):
        pass


class DES_Image_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Diagram showing the Structure of DES",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        try:
            img = Image.open("./images/DES_Drawing.png")
            img = ImageTk.PhotoImage(img.resize((300, 400)))
            label = Label(self, image=img)
            label.image = img
            label.pack(ipady=20)
        except Exception as inst:
            print(inst)
            print(os.listdir())
            label = Label(self, text="IMAGE MISSING", font=("Arial", 15))
            label.pack()

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Disclaimer_Page"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

    def updateText(self):
        pass


class DES_Disclaimer_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Disclaimer about the DES Visualisation",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        disclaimer_text = "\nThe program does not show each round performed by the DES cipher but instead visualises " \
                          "the first round of every encryption/decryption,\nas to learn the cipher only one round " \
                          "needs to be visualised. The diagram below shows what this program actually visualises.\n"
        disclaimer_label = Label(self, text=disclaimer_text, font=("Calibri", 15))
        disclaimer_label.pack()

        try:
            img = Image.open("./images/DES_Disclaimer_Drawing.png")
            img = ImageTk.PhotoImage(img.resize((300, 350)))
            label = Label(self, image=img)
            label.image = img
            label.pack()
        except Exception as inst:
            print(inst)
            print(os.listdir())
            label = Label(self, text="IMAGE MISSING", font=("Arial", 15))
            label.pack()

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Page"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

    def updateText(self):
        pass


class DES_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        plaintext = self.controller.shared_data["plaintext"]
        key = self.controller.shared_data["key"]

        title_label = Label(self, text="DES Page", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        input_label = Label(self, text="Input 64-Bit String:", font=("Calibri", 20), fg="black")
        input_label.pack(expand=True)

        input_entry = Entry(self, textvariable=plaintext, bg='white', font=("Arial", 10))
        input_entry.pack(ipadx=155, ipady=10, expand=True)
        input_entry.focus()
        self.input_entry = input_entry
        input_reg = self.register(self.input_callback)
        input_entry.config(validate="key", validatecommand=(input_reg, '%P'))

        random_input = Button(self, text="Random Plaintext", bg='#cf3030', fg="white", font=("Arial", 10),
                              command=lambda: self.make_random_plaintext())
        random_input.pack(ipadx=20, ipady=10, expand=True, fill="none")

        key_label = Label(self, text="Enter Key:", font=("Calibri", 20), fg="black")
        key_label.pack(expand=True)

        key_entry = Entry(self, textvariable=key, bg='white', font=("Arial", 10))
        key_entry.pack(ipadx=100, ipady=10, expand=True)
        self.key_entry = key_entry
        key_reg = self.register(self.key_callback)
        key_entry.config(validate="key", validatecommand=(key_reg, '%P'))

        random_key = Button(self, text="Random Key", bg='#cf3030', fg="white", font=("Arial", 10),
                            command=lambda: self.make_random_key())
        random_key.pack(ipadx=10, ipady=10, expand=True, fill="none")

        encrypt_button = Button(self, text="Encrypt", font=("Arial", 20), bg="#e88a1a", fg="white",
                                command=lambda: self.num_check(controller, True))
        encrypt_button.pack(ipadx=10, ipady=10, expand=True, fill="none", side=LEFT)

        decrypt_button = Button(self, text="Decrypt", font=("Arial", 20), bg="#e88a1a", fg="white",
                                command=lambda: self.num_check(controller, False))
        decrypt_button.pack(ipadx=10, ipady=10, expand=True, fill="none", side=RIGHT)

    def initial_perm(self, controller):
        plaintext = self.controller.shared_data["plaintext"].get()
        permuted_text = des_logic.initial_perm(list(plaintext))
        self.controller.shared_data["initial_permutation"] = permuted_text
        controller.show_frame("DES_Encrypt_Page_1")

    def updateText(self):
        pass

    def make_random_plaintext(self):
        random_text = ""
        for x in range(0, 64):
            random_text += str(random.randint(0, 1))
        self.input_entry.delete(0, END)
        self.input_entry.insert(0, random_text)

    def make_random_key(self):
        random_key = ""
        for x in range(0, 48):
            random_key += str(random.randint(0, 1))
        self.key_entry.delete(0, END)
        self.key_entry.insert(0, random_key)

    def input_callback(self, input):
        if len(input) > 64:
            messagebox.showwarning("Visualisation Tool", message="Reached 64 bits\nMessage too long")
            return False
        elif input.isdigit() or input == "":
            if int(input[len(input) - 1]) > 1:
                messagebox.showwarning("Visualisation Tool", message="Can only enter digits: 0, 1")
                return False
            return True
        else:
            messagebox.showwarning("Visualisation Tool", message="Can only enter digits: 0, 1")
            return False

    def key_callback(self, input):
        if len(input) > 48:
            messagebox.showwarning("Visualisation Tool", message="Reached 48 bits\nMessage too long")
            return False
        elif input.isdigit() or input == "":
            if int(input[len(input) - 1]) > 1:
                messagebox.showwarning("Visualisation Tool", message="Can only enter digits: 0, 1")
                return False
            return True
        else:
            messagebox.showwarning("Visualisation Tool", message="Can only enter digits")
            return False

    def num_check(self, controller, encrypt):
        plaintext = self.controller.shared_data["plaintext"].get()
        key = self.controller.shared_data["key"].get()

        if len(plaintext) != 64 or len(key) != 48:
            messagebox.showwarning("Visualisation Tool", "Input lengths are wrong\nCheck inputs for length\n"
                                                         "Plaintext/Ciphertext must be 64 bits long\n"
                                                         "Key must be 48 bits long")
            return False
        if encrypt:
            self.initial_perm(controller)
        if not encrypt:
            controller.show_frame("DES_Decrypt_Page_1")


class DES_Encrypt_Page_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        permutation_order_no_1 = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 28, 12,
                                  4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16,
                                  8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11,
                                  3, 61, 33, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]

        title_label = Label(self, text="Initial Permutation", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nThe first step of encryption is to change the position of the data according to the order" \
                           " shown below.\n\nFor example, the 58th bit is moved to the first position.\n\n\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack()

        input_label = Label(self, bg="orange")
        input_label.pack()
        self.input_label = input_label

        permuted_label = Label(self, text=("Permutation Order\n" + str(permutation_order_no_1)), font=("Calibri", 9))
        permuted_label.pack(expand=True)

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Encrypt_Page_2"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

    def updateText(self):
        plaintext = self.controller.shared_data["plaintext"].get()
        permuted_plaintext = self.controller.shared_data["initial_permutation"]
        updated_label = Label(self.input_label, text=(plaintext + "\n→\n" + ''.join(permuted_plaintext)),
                              font=("Calibri", 17))
        updated_label.pack(expand=True, side=TOP)


class DES_Encrypt_Page_2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Splitting in half of permuted plaintext",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nThe right and left side are split. This is because the right side will go through " \
                           "several stages to encrypt it.\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack()

        next_button = Button(self, text="NEXT", command=lambda: self.expand_right(controller),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

        input_label = Label(self)
        input_label.pack()
        self.input_label = input_label

        left_side = Label(self, bg="orange")
        left_side.pack(expand=1, side='left')
        self.left_side = left_side

        right_side = Label(self, bg="orange")
        right_side.pack(expand=1, side='left')
        self.right_side = right_side

    def updateText(self):
        initial_perm = self.controller.shared_data["initial_permutation"]
        self.controller.shared_data["initial_left_side"] = initial_perm[0:32]

        updated_input_label = Label(self.input_label, text="Plaintext:\n" + ''.join(initial_perm), font=("Calibri", 14))
        updated_input_label.pack()

        left_side_text = "Left Side:\n" + ' '.join(self.controller.shared_data["initial_left_side"])
        updated_left_side = Label(self.left_side, text=left_side_text,
                                  font=("Calibri", 14))
        updated_left_side.pack(expand=1, side='left', ipadx=10)

        right_side_text = "Right Side:\n" + ' '.join(initial_perm[32:64])
        updated_right_side = Label(self.right_side, text=right_side_text, font=("Calibri", 14))
        updated_right_side.pack(expand=1, side='left', ipadx=10)

    def expand_right(self, controller):
        initial_perm = self.controller.shared_data["initial_permutation"]

        self.controller.shared_data["right_side"] = initial_perm[32:64]
        self.controller.shared_data["changed_right_side"] = \
            des_logic.right_side_expansion(self.controller.shared_data["right_side"])

        controller.show_frame("DES_Encrypt_Page_3")


class DES_Encrypt_Page_3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Expansion of Right side", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nThe right side is expanded from 32-bits to 48-bits, " \
                           "based on the expansion order shown below.\n\nRight Side → Expanded Right Side\n\n"

        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack()

        expansion_label = Label(self, bg="orange")
        expansion_label.pack()
        self.expansion_label = expansion_label

        expansion_order = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18,
                           19, 20,
                           21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

        permutation_order_label = Label(self, text=("Expansion Order\n" + str(expansion_order)), font=("Calibri", 13))
        permutation_order_label.pack(expand=1)

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Encrypt_Page_4"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        right_side = self.controller.shared_data["right_side"]
        right_side = ' '.join(right_side)

        right_after_expansion = self.controller.shared_data["changed_right_side"]
        right_after_expansion = ' '.join(right_after_expansion)

        text = right_side + "\n→\n" + right_after_expansion

        updated_expansion_label = Label(self.expansion_label, text=text, font=("Calibri", 17))
        updated_expansion_label.pack()


class DES_Encrypt_Page_4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Expanded Right Side XORed with Key",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nThe expanded right side is XORed with the subkey\n\n" \
                           "RIGHT AFTER EXPANSION  ⊕  SUBKEY  →  RESULT\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack(ipady=25)

        right_label = Label(self, bg="orange")
        right_label.pack()
        self.right_label = right_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Encrypt_Page_5"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        right_side = self.controller.shared_data["changed_right_side"]

        key = self.controller.shared_data["key"].get()

        xored_right = des_logic.right_xor_key(right_side, key)
        self.controller.shared_data["changed_right_side"] = xored_right

        right_label_text = ''.join(right_side) + "\n⊕\n" + key + "\n→\n" + ''.join(xored_right)
        updated_right_label = Label(self.right_label, text=right_label_text, font=("Calibri", 17))
        updated_right_label.pack(ipadx=10)


class DES_Encrypt_Page_5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="S Box", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = \
            "Right side is split into 8 6-bit blocks. The first and last digits of each block are combined as well " \
            "as the middle digits to get 2 decimal numbers. \n\n" \
            "Based on these values a number is found in the lookup table, of which each block has a separate one. " \
            "This number is the new value for the the block.\n\n" \
            "Therefore, there will now be 8 4-bit blocks meaning there are 32-bits on the right side now, " \
            "not 48 (the number of bits after the expansion)"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 13))
        explanation_label.pack()

        right_after_e_xor_label = Label(self, text="RIGHT AFTER EXPANSION AND XOR")
        right_after_e_xor_label.pack()
        self.right_after_e_xor_label = right_after_e_xor_label

        right_split_label = Label(self, text="RIGHT SIDE SPLIT IN 6-BIT BLOCKS")
        right_split_label.pack()
        self.right_split_label = right_split_label

        first_block_label = Label(self)
        first_block_label.pack()
        self.first_block_label = first_block_label

        first_block_first_and_last_bit_label = Label(
            self)  # FIRST AND LAST BIT OF THE FIRST BLOCK GO HERE = THEIR VALUE IN DECIMAL
        first_block_first_and_last_bit_label.pack()
        self.first_block_first_and_last_bit_label = first_block_first_and_last_bit_label

        middle_bits_of_first_block_label = Label(self)  # MIDDLE BITS OF FIRST BLOCK GO HERE = THERE VALUE IN DECIMAL

        middle_bits_of_first_block_label.pack()
        self.middle_bits_of_first_block_label = middle_bits_of_first_block_label

        shrunk_right_side_label = Label(self, text="8-4Bit BLOCKS", bg="orange")
        shrunk_right_side_label.pack()
        self.shrunk_right_side_label = shrunk_right_side_label

        lookup_table_1 = [
            ["1110", "0100", "1101", "0001", "0010", "1111", "1011", "1000", "0011", "1010", "0110", "1100",
             "0101", "1001", "0000", "0111"],
            ["0000", "1111", "0111", "0100", "1110", "0010", "1101", "0001", "1010", "0110", "1100", "1011",
             "1001", "0101", "0011", "1000"],
            ["0100", "0001", "1110", "1000", "1101", "0110", "0010", "1011", "1111", "1100", "1001", "0111",
             "0011", "1010", "0101", "0000"],
            ["1111", "1100", "1000", "0010", "0100", "1001", "0001", "0111", "0101", "1011", "0011", "1110",
             "1010", "0000", "0110", "1101"]]

        lookup_table_text = "First Block Lookup Table\n"

        for rows in range(0, 4):
            for columns in range(0, 16):
                lookup_table_text += lookup_table_1[rows][columns]
                lookup_table_text += "  "
            if rows != 3:
                lookup_table_text += "\n"

        lookup_table_Label = Label(self, text=lookup_table_text, font=("Calibri", 11))
        lookup_table_Label.pack(fill='x')

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Encrypt_Page_6"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

    def updateText(self):
        right_side = self.controller.shared_data["changed_right_side"]
        six_bit_label_text = ""
        six_bit_label_array = []
        for x in range(0, 48, 6):
            for z in range(0, 6):
                six_bit_label_text += right_side[x + z]
            six_bit_label_array.append(six_bit_label_text)
            six_bit_label_text += "  "

        # Initial text- right side that has been expanded and xored
        updated_right_after_e_xor_label = Label(self.right_after_e_xor_label,
                                                text=("Right Side\n" + ' '.join(right_side)),
                                                font=("Calibri", 12))
        updated_right_after_e_xor_label.pack()

        # Same text as above but has been split to show the 6 blocks
        updated_right_split_label = Label(self.right_split_label,
                                          text="Segmented Right Side\n" + ' '.join(six_bit_label_text),
                                          font=("Calibri", 12))
        updated_right_split_label.pack()

        # First block
        first_block_text = six_bit_label_array[0]
        updated_first_block_label = Label(self.first_block_label, text="First Block\n" + ' '.join(first_block_text),
                                          font=("Calibri", 12))
        updated_first_block_label.pack()

        # First and Last bit of the first block and their decimal value
        first_block_first_and_last_bit_text = six_bit_label_array[0][0] + six_bit_label_array[0][5]
        first_block_first_and_last_bit_text += " = " + get_decimal_value(first_block_first_and_last_bit_text)
        updated_first_block_first_and_last_bit_label = Label(self.first_block_first_and_last_bit_label,
                                                             text="First Block: First and Last Bit\n" +
                                                                  ' '.join(first_block_first_and_last_bit_text),
                                                             font=("Calibri", 12))
        updated_first_block_first_and_last_bit_label.pack()

        # Middle 4 bits of the first block and their decimal value
        middle_bits_of_first_block_text = six_bit_label_array[0][1] + six_bit_label_array[0][2] + \
                                          six_bit_label_array[0][3] + six_bit_label_array[0][4]
        middle_bits_of_first_block_text += " = " + get_decimal_value(middle_bits_of_first_block_text)
        updated_middle_bits_of_first_block_label = Label(self.middle_bits_of_first_block_label,
                                                         text="First Block: Middle Bits\n" +
                                                              ' '.join(middle_bits_of_first_block_text),
                                                         font=("Calibri", 12))
        updated_middle_bits_of_first_block_label.pack()

        # Shrunk version of the right side after going through the s_box
        shrunk_right_side = des_logic.s_box(right_side)
        updated_shrunk_right_label = Label(self.shrunk_right_side_label, text="Shrunk Right Side\n" +
                                                                              ' '.join(shrunk_right_side),
                                           font=("Calibri", 12))
        updated_shrunk_right_label.pack()
        self.controller.shared_data["changed_right_side"] = shrunk_right_side


class DES_Encrypt_Page_6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Right Side Permutation", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nThe right side is permuted based on the permutation order shown below. For example, " \
                           "the 1st place bit is replaced by the 16th place bit.\n\n" \
                           "8 4-Bit RIGHT SIDE  →  PERMUTED RIGHT SIDE\n\n\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack()

        right_side_and_permutation_label = Label(self, bg="orange")
        right_side_and_permutation_label.pack()
        self.right_side_and_permutation_label = right_side_and_permutation_label

        permutation_order_no_2 = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 8, 31, 10, 2, 8, 24, 14, 32, 27,
                                  3, 9, 19, 13, 30, 6, 22, 11, 4, 25]

        permutation_order_label = Label(self, text=("\nPERMUTATION ORDER\n" + str(permutation_order_no_2)),
                                        font=("Calibri", 16))
        permutation_order_label.pack(expand=True)

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Encrypt_Page_7"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        right_side = self.controller.shared_data["changed_right_side"]
        permuted_right_side = des_logic.second_permutation(right_side)

        right_side_and_permutation_text = ' '.join(right_side) + "\n→\n" + ' '.join(permuted_right_side)
        updated_right_side_and_permutation_label = Label(self.right_side_and_permutation_label,
                                                         text=right_side_and_permutation_text,
                                                         font=("Calibri", 17))
        updated_right_side_and_permutation_label.pack()

        self.controller.shared_data["changed_right_side"] = permuted_right_side


class DES_Encrypt_Page_7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Right Side XORed with Initial Left Side",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "The Left side and the Right side are XORed together. The result of this calculation is " \
                           "to become the Left Side of the Ciphertext.\n\n" \
                           "RIGHT SIDE  ⊕  LEFT SIDE  →  NEW LEFT SIDE\n\n\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack(ipady=20)

        right_side_xored_with_left_side_label = Label(self, bg="orange")
        right_side_xored_with_left_side_label.pack()
        self.right_side_xored_with_left_side_label = right_side_xored_with_left_side_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Encrypt_Page_8"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        right_side = self.controller.shared_data["changed_right_side"]
        left_side = self.controller.shared_data["initial_left_side"]
        new_right = des_logic.right_xor_left(right_side, left_side)

        right_side_xored_with_left_side_text = ' '.join(right_side) + "  ⊕  " + ' '.join(left_side) + "\n→\n" + \
                                               ' '.join(new_right)

        updated_right_side_xored_with_left_side_label = Label(self.right_side_xored_with_left_side_label,
                                                              text=right_side_xored_with_left_side_text,
                                                              font=("Calibri", 17))
        updated_right_side_xored_with_left_side_label.pack()

        self.controller.shared_data["changed_right_side"] = new_right


class DES_Encrypt_Page_8(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Merging of Left and Right Side to make Ciphertext",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "The left side of the ciphertext is the result of the permuted right side being " \
                           "encrypted and the right side is the value of the permuted right side."
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack(ipady=10)

        left_block_label = Label(self)
        left_block_label.pack()
        self.left_block_label = left_block_label

        right_block_label = Label(self)
        right_block_label.pack()
        self.right_block_label = right_block_label

        ciphertext_label = Label(self, bg="orange")
        ciphertext_label.pack()
        self.ciphertext_label = ciphertext_label

    def updateText(self):
        left_side = self.controller.shared_data["changed_right_side"]
        right_side = self.controller.shared_data["right_side"]
        ciphertext = left_side + right_side

        left_block_text = "LEFT SIDE:\n" + ' '.join(left_side)
        updated_left_block_label = Label(self.left_block_label, text=left_block_text, font=("Calibri", 17))
        updated_left_block_label.pack(ipady=20)

        right_block_text = "RIGHT SIDE: \n" + ' '.join(right_side)
        updated_right_block_label = Label(self.right_block_label, text=right_block_text, font=("Calibri", 17))
        updated_right_block_label.pack(ipady=20)

        ciphertext_text = "CIPHERTEXT: \n" + ' '.join(ciphertext)
        updated_ciphertext_label = Label(self.ciphertext_label, text=ciphertext_text, font=("Calibri", 18))
        updated_ciphertext_label.pack(ipady=20)


class DES_Decrypt_Page_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Splitting of Left and Right Side of Ciphertext ",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nThe text is split in half. This is because the right side will go through several steps " \
                           "different to the left side.\n\nBy having the right side go through the same steps it did " \
                           "to encrypt it, the original permuted left side can be found by\n\nXORing the result of " \
                           "the right side going through the encryption steps and the ciphertext’s left side.\n\n" \
                           "Since the original permuted right side is the same as the ciphertext’s right side, " \
                           "the original permuted plaintext can be found.\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack()

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Decrypt_Page_2"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

        ciphertext_label = Label(self)
        ciphertext_label.pack()
        self.ciphertext_label = ciphertext_label

        left_side_label = Label(self, bg="orange")
        left_side_label.pack(expand=1, side='left', ipadx=10)
        self.left_side_label = left_side_label

        right_side_label = Label(self, bg="orange")
        right_side_label.pack(expand=1, side='right', ipadx=10)
        self.right_side_label = right_side_label

    def updateText(self):
        ciphertext = self.controller.shared_data["plaintext"].get()
        left_side = ciphertext[:(len(ciphertext) // 2)]
        right_side = ciphertext[(len(ciphertext) // 2):]

        left_side_label = "Left Side:\n" + ' '.join(left_side)
        right_side_label = "Right Side:\n" + ' '.join(right_side)

        updated_ciphertext_label = Label(self.ciphertext_label, text="Ciphertext:\n" + ' '.join(ciphertext),
                                         font=("Calibri", 14))
        updated_ciphertext_label.pack()

        updated_left_side_label = Label(self.left_side_label, text=left_side_label, font=("Calibri", 14))
        updated_left_side_label.pack(expand=1, fill='x', side='left', ipadx=10)

        updated_right_side_label = Label(self.right_side_label, text=right_side_label, font=("Calibri", 14))
        updated_right_side_label.pack(expand=1, fill='x', side='right', ipadx=10)

        self.controller.shared_data["decryption_right_side"] = right_side
        self.controller.shared_data["decryption_left_side"] = left_side


class DES_Decrypt_Page_2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Expansion of the Right Side", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nThe right side is expanded from 32-bits to 48-bits, based on the expansion order shown " \
                           "below.\nAs can be seen, several values are repeated to expand the right side.\n\n" \
                           "Right Side → Expanded Right Side\n\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack()

        expansion_label = Label(self, bg="orange")
        expansion_label.pack()
        self.expansion_label = expansion_label

        expansion_order = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18,
                           19, 20,
                           21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]

        permutation_order_label = Label(self, text=("Expansion Order\n" + str(expansion_order)), font=("Calibri", 13))
        permutation_order_label.pack(expand=1)

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Decrypt_Page_3"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        right_side = self.controller.shared_data["decryption_right_side"]
        expanded_right_side = des_logic.right_side_expansion(right_side)
        self.controller.shared_data["decryption_changed_right_side"] = expanded_right_side

        expansion_text = ' '.join(right_side) + "\n→\n" + ' '.join(expanded_right_side)
        updated_expansion_label = Label(self.expansion_label, text=expansion_text, font=("Calibri", 17))
        updated_expansion_label.pack()


class DES_Decrypt_Page_3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Expanded Right Side XORed with Key",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "The expanded right side is XORed with the subkey\n\n" \
                           "RIGHT AFTER EXPANSION  ⊕  SUBKEY  →  RESULT\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack(ipady=40)

        xored_right_label = Label(self, bg="orange")
        xored_right_label.pack()
        self.xored_right_label = xored_right_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Decrypt_Page_4"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        right_side = self.controller.shared_data["decryption_changed_right_side"]
        key = self.controller.shared_data["key"].get()
        xored_right_side = des_logic.right_xor_key(right_side, key)
        self.controller.shared_data["decryption_changed_right_side"] = xored_right_side

        xored_right_text = ' '.join(right_side) + "\n⊕\n" + ' '.join(key) + "\n→\n" + ' '.join(xored_right_side)
        updated_xored_right_label = Label(self.xored_right_label, text=xored_right_text, font=("Calibri", 17))
        updated_xored_right_label.pack(ipadx=10)


class DES_Decrypt_Page_4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="S Box", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = \
            "Right side is split into 8 6-bit blocks. The first and last digits of each block are combined as well " \
            "as the middle digits to get 2 decimal numbers. \n\n" \
            "Based on these values a number is found in the lookup table, of which each block has a separate one. " \
            "This number is the new value for the the block.\n\n" \
            "Therefore, there will now be 8 4-bit blocks meaning there are 32-bits on the right side now, " \
            "not 48 (the number of bits after the expansion)"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 13))
        explanation_label.pack()

        right_side_label = Label(self, text="ciphertext")
        right_side_label.pack()
        self.right_side_label = right_side_label

        segmented_right_side_label = Label(self)
        segmented_right_side_label.pack()
        self.segmented_right_side_label = segmented_right_side_label

        first_block_label = Label(self)
        first_block_label.pack()
        self.first_block_label = first_block_label

        first_block_first_and_last_bits = Label(self)
        first_block_first_and_last_bits.pack()
        self.first_block_first_and_last_bits = first_block_first_and_last_bits

        first_block_middle_bits = Label(self)
        first_block_middle_bits.pack()
        self.first_block_middle_bits = first_block_middle_bits

        shrunk_right_side = Label(self, bg="orange")
        shrunk_right_side.pack()
        self.shrunk_right_side = shrunk_right_side

        first_block_lookup_table = [
            ["1110", "0100", "1101", "0001", "0010", "1111", "1011", "1000", "0011", "1010", "0110", "1100",
             "0101", "1001", "0000", "0111"],
            ["0000", "1111", "0111", "0100", "1110", "0010", "1101", "0001", "1010", "0110", "1100", "1011",
             "1001", "0101", "0011", "1000"],
            ["0100", "0001", "1110", "1000", "1101", "0110", "0010", "1011", "1111", "1100", "1001", "0111",
             "0011", "1010", "0101", "0000"],
            ["1111", "1100", "1000", "0010", "0100", "1001", "0001", "0111", "0101", "1011", "0011", "1110",
             "1010", "0000", "0110", "1101"]]

        lookup_table_text = "First Block Lookup Table\n"

        for rows in range(0, 4):
            for columns in range(0, 16):
                lookup_table_text += first_block_lookup_table[rows][columns]
                lookup_table_text += "  "
            if rows != 3:
                lookup_table_text += "\n"

        lookup_table_Label = Label(self, text=lookup_table_text, font=("Calibri", 11))
        lookup_table_Label.pack(fill='x')

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Decrypt_Page_5"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

    def updateText(self):
        right_side = self.controller.shared_data["decryption_changed_right_side"]

        six_bit_label_text = ""
        six_bit_label_array = []

        for x in range(0, 48, 6):
            for z in range(0, 6):
                six_bit_label_text += right_side[x + z]
            six_bit_label_array.append(six_bit_label_text)
            six_bit_label_text += "  "

        updated_right_side_label = Label(self.right_side_label, text=("Right Side\n" + ' '.join(right_side)),
                                         font=("Calibri", 12))
        updated_right_side_label.pack()

        updated_segmented_right_side_label = Label(self.segmented_right_side_label,
                                                   text=("Segmented Left Side\n" + ' '.join(six_bit_label_text)),
                                                   font=("Arial", 12))
        updated_segmented_right_side_label.pack()

        updated_first_block_label = Label(self.first_block_label,
                                          text="First Block:\n" + ' '.join(six_bit_label_array[0]),
                                          font=("Calibri", 12))
        updated_first_block_label.pack()

        first_block_first_and_last_bits_text = six_bit_label_array[0][0] + six_bit_label_array[0][5]
        first_block_first_and_last_bits_text += " = " + get_decimal_value(first_block_first_and_last_bits_text)
        updated_first_block_first_and_last_bits = Label(self.first_block_first_and_last_bits,
                                                        text="First Block: First and Last Bits\n" +
                                                             ' '.join(first_block_first_and_last_bits_text),
                                                        font=("Arial", 12))
        updated_first_block_first_and_last_bits.pack()

        first_block_middle_bits_text = six_bit_label_array[0][1] + six_bit_label_array[0][2] + \
                                       six_bit_label_array[0][3] + six_bit_label_array[0][4]
        first_block_middle_bits_text += " = " + get_decimal_value(first_block_middle_bits_text)
        updated_first_block_middle_bits = Label(self.first_block_middle_bits,
                                                text="First Block: Middle Bits\n" +
                                                     ' '.join(first_block_middle_bits_text),
                                                font=("Calibri", 12))
        updated_first_block_middle_bits.pack()

        shrunk_right_side = des_logic.s_box(right_side)
        updated_shrunk_right_side = Label(self.shrunk_right_side,
                                          text=("Shrunk Right Side: \n" + ' '.join(shrunk_right_side)),
                                          font=("Calibri", 12))
        updated_shrunk_right_side.pack()

        self.controller.shared_data["decryption_changed_right_side"] = shrunk_right_side


class DES_Decrypt_Page_5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Permutation of Right side", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nThe right side is permuted based on the permutation order shown below.\nFor example, " \
                           "the 1st place bit is replaced by the 16th place bit.\n\n" \
                           "8 4-Bit RIGHT SIDE  →  PERMUTED RIGHT SIDE\n\n\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack()

        permutation_label = Label(self, bg="orange")
        permutation_label.pack()
        self.permutation_label = permutation_label

        permutation_order_no_2 = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 8, 31, 10, 2, 8, 24, 14, 32, 27,
                                  3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
        permutation_table_label = Label(self, text=("\nPermutation Order:\n" + str(permutation_order_no_2)),
                                        font=("Calibri", 16))
        permutation_table_label.pack(expand=True)

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Decrypt_Page_6"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        right_side = self.controller.shared_data["decryption_changed_right_side"]
        permuted_right_side = des_logic.second_permutation(right_side)

        permutation_text = ' '.join(right_side) + "\n→\n" + ' '.join(permuted_right_side)
        updated_permutation_label = Label(self.permutation_label, text=permutation_text, font=("Calibri", 17))
        updated_permutation_label.pack(ipady=10)

        self.controller.shared_data["decryption_changed_right_side"] = permuted_right_side


class DES_Decrypt_Page_6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Left Side XORed with Right Side", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "The Left side and the Right side are XORed together. The result of this calculation is " \
                           "to become the Left Side of the Plaintext.\n\n" \
                           "RIGHT SIDE  ⊕  LEFT SIDE  →  NEW LEFT SIDE\n\n\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack(ipady=20)

        visualisation_label = Label(self, bg="orange")
        visualisation_label.pack()
        self.visualisation_label = visualisation_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Decrypt_Page_7"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        left_side = self.controller.shared_data["decryption_left_side"]
        right_side = self.controller.shared_data["decryption_changed_right_side"]
        new_left = des_logic.right_xor_left(right_side, left_side)

        visualisation_text = ' '.join(left_side) + "\n⊕\n" + ' '.join(right_side) + "\n→\n" + ' '.join(new_left)
        updated_visualisation_label = Label(self.visualisation_label, text=visualisation_text, font=("Calibri", 17))
        updated_visualisation_label.pack(ipadx=10)

        self.controller.shared_data["decryption_changed_left_side"] = new_left


class DES_Decrypt_Page_7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Concatenating of Calculated Left Side and Given Right Side",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nBy combining the result of the calculations, i.e. the left side, and the ciphertext’s " \
                           "right side, the original permuted right side is found.\nThe last step then, is to undo " \
                           "the initial permutation used to encrypt the data.\n\n" \
                           "Merged Left and Right Side → Original Plaintext\n\n\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack()

        left_and_right_side_label = Label(self)
        left_and_right_side_label.pack()
        self.left_and_right_side_label = left_and_right_side_label

        result_label = Label(self)
        result_label.pack()
        self.result_label = result_label

        plaintext_label = Label(self, bg="orange")
        plaintext_label.pack(side=BOTTOM)
        self.plaintext_label = plaintext_label

        permutation_order_no_1 = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 28, 12,
                                  4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16,
                                  8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11,
                                  3, 61, 33, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
        permutation_order_label = Label(self, text=("\nPermutation Order:\n" + str(permutation_order_no_1)),
                                        font=("Calibri", 9))
        permutation_order_label.pack()

    def updateText(self):
        left_side = self.controller.shared_data["decryption_changed_left_side"]
        right_side = list(self.controller.shared_data["decryption_right_side"])
        left_and_right_side = left_side + right_side

        left_and_right_side_text = ' '.join(left_side + right_side) + "\n→"

        plaintext = des_logic.undo(left_and_right_side)

        updated_left_and_right_side_label = Label(self.left_and_right_side_label,
                                                  text=left_and_right_side_text,
                                                  font=("Calibri", 14))
        updated_left_and_right_side_label.pack()

        updated_result_label = Label(self.result_label, text=' '.join(plaintext), font=("Calibri", 14))
        updated_result_label.pack()

        updated_plaintext_label = Label(self.plaintext_label, text=("Plaintext: \n" + ' '.join(plaintext)),
                                        font=("Calibri", 17))
        updated_plaintext_label.pack(side=BOTTOM)


class AES_Info_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="AES", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        label_1_text = "The Advanced Encryption Standard (AES) is a Symmetric Key Block Cipher established in 2001\n"
        label_1 = Label(self, text=label_1_text, font=("Calibri", 15), anchor='w')
        label_1.pack()

        input_text = "Inputs: 128-bit Plaintext and 128/192/256-bit Key"
        inputs_label = Label(self, text=input_text, font=("Calibri", 15), anchor='w')
        inputs_label.pack()

        output_text = "Output: 128-bit Ciphertext.\n"
        output_label = Label(self, text=output_text, font=("Calibri", 15), anchor='w')
        output_label.pack()

        label_2_text = "It is an implementation of a Substitution Permutation Network,\nmeaning that to reverse the " \
                       "process, inverse of each step can be applied in the reverse order.\n"
        label_2 = Label(self, text=label_2_text, font=("Calibri", 15), anchor='w')
        label_2.pack()

        label_3_text = "For an 128-bit Key there are 10 rounds (12 for 192 and 14 for 256)\n"
        label_3 = Label(self, text=label_3_text, font=("Calibri", 15), anchor='w')
        label_3.pack()

        process_text = "To encrypt the plaintext is first XORed by the initial round key and then goes " \
                       "through several stages for each round"
        process_label = Label(self, text=process_text, font=("Calibri", 15))
        process_label.pack()

        label_4_text = "Each round is made up of 5 Steps:"
        label_4 = Label(self, text=label_4_text, font=("Calibri", 15), anchor='w')
        label_4.pack()

        step_1_text = "1. Substitute the bytes in the Plaintext."
        step_1_label = Label(self, text=step_1_text, font=("Calibri", 15), anchor='w')
        step_1_label.pack()

        step_2_text = "2. Shift the rows accordingly."
        step_2_label = Label(self, text=step_2_text, font=("Calibri", 15), anchor='w')
        step_2_label.pack()

        step_3_text = "3. Mix the columns by multiplying them by a certain matrix."
        step_3_label = Label(self, text=step_3_text, font=("Calibri", 15), anchor='w')
        step_3_label.pack()

        step_4_text = "4. Add the round key by XORing it with the plaintext."
        step_4_label = Label(self, text=step_4_text, font=("Calibri", 15), anchor='w')
        step_4_label.pack()

        step_5_text = "5. On the last round, repeat all these steps except for the mix columns step."
        step_5_label = Label(self, text=step_5_text, font=("Calibri", 15), anchor='w')
        step_5_label.pack()

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("AES_Image_Page"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

    def updateText(self):
        pass


class AES_Image_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Structure of AES", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        try:
            img = Image.open("./images/AES_Drawing.png")
            img = ImageTk.PhotoImage(img.resize((750, 400)))
            label = Label(self, image=img)
            label.image = img
            label.pack(ipady=10)
        except Exception as inst:
            print(inst)
            print(os.listdir())
            label = Label(self, text="IMAGE MISSING", font=("Arial", 15))
            label.pack()

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("AES_Disclaimer_Page"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

    def updateText(self):
        pass


class AES_Disclaimer_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Disclaimer about the DES Visualisation",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        disclaimer_text = "The program does not show each round performed by the AES cipher but instead visualises " \
                          "the first round of every encryption/decryption,\nas to help learn the cipher only one " \
                          "round needs to be visualised. The diagram below shows what this program actually visualises."
        disclaimer_label = Label(self, text=disclaimer_text, font=("Calibri", 15))
        disclaimer_label.pack()

        try:
            img = Image.open("./images/AES_Disclaimer_Drawing.png")
            img = ImageTk.PhotoImage(img.resize((700, 400)))
            label = Label(self, image=img)
            label.image = img
            label.pack(ipady=10)
        except Exception as inst:
            print(inst)
            print(os.listdir())
            label = Label(self, text="IMAGE MISSING", font=("Arial", 15))
            label.pack()

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("AES_Page"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

    def updateText(self):
        pass


class AES_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        reg = self.register(self.callback)

        input = self.controller.shared_data["AES_input"]
        key_1 = self.controller.shared_data["AES_key_1"]
        key_2 = self.controller.shared_data["AES_key_2"]

        title_label = Label(self, text="AES Page", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        input_label = Label(self, text="Input 16-Byte Hex String:", font=("Arial", 20), fg="black")
        input_label.pack(expand=True)

        input_entry = Entry(self, textvariable=input, bg='white', font=("Arial", 10))
        input_entry.pack(ipadx=155, ipady=10, expand=True)
        input_entry.focus()
        self.input_entry = input_entry
        input_entry.config(validate="key", validatecommand=(reg, '%P'))

        random_input = Button(self, text="Random Plaintext", bg='#cf3030', fg="white", font=("Arial", 10),
                              command=lambda: self.make_random(input_entry))
        random_input.pack(ipadx=20, ipady=10, expand=True, fill="none")

        key_label_1 = Label(self, text="Enter Key:", font=("Arial", 20), fg="black")
        key_label_1.pack(expand=True)

        key_entry_1 = Entry(self, bg='white', textvariable=key_1, font=("Arial", 10))
        key_entry_1.pack(ipadx=100, ipady=10, expand=True)
        self.key_entry_1 = key_entry_1
        key_entry_1.config(validate="key", validatecommand=(reg, '%P'))

        random_key_1 = Button(self, text="Random Key", bg='#cf3030', fg="white", font=("Arial", 10),
                              command=lambda: self.make_random(key_entry_1))
        random_key_1.pack(ipadx=10, ipady=10, expand=True, fill="none")

        key_label_2 = Label(self, text="Enter Key:", font=("Arial", 20), fg="black")
        key_label_2.pack(expand=True)

        key_entry_2 = Entry(self, bg='white', textvariable=key_2, font=("Arial", 10))
        key_entry_2.pack(ipadx=100, ipady=10, expand=True)
        self.key_entry_2 = key_entry_2
        key_entry_2.config(validate="key", validatecommand=(reg, '%P'))

        random_key_2 = Button(self, text="Random Key", bg='#cf3030', fg="white", font=("Arial", 10),
                              command=lambda: self.make_random(key_entry_2))
        random_key_2.pack(ipadx=10, ipady=10, expand=True, fill="none")

        encrypt_button = Button(self, text="Encrypt", font=("Arial", 20), bg="#e88a1a", fg="white",
                                command=lambda: self.num_check(controller, True))
        encrypt_button.pack(ipadx=10, ipady=10, expand=True, fill="none", side=LEFT)

        decrypt_button = Button(self, text="Decrypt", font=("Arial", 20), bg="#e88a1a", fg="white",
                                command=lambda: self.num_check(controller, False))
        decrypt_button.pack(ipadx=10, ipady=10, expand=True, fill="none", side=RIGHT)

    def updateText(self):
        pass

    def make_random(self, entry):
        random_text = hex(random.randint(0, 340282366920938463463374607431768211455))
        random_text = aes_logic.add_padding(random_text, 32)
        entry.delete(0, END)
        entry.insert(0, random_text)

    def callback(self, input):
        if len(input) > 32:
            messagebox.showwarning("Visualisation Tool", message="Reached 32 Bytes\nMessage too long")
            return False
        elif all(c in string.hexdigits for c in input):
            return True
        else:
            messagebox.showwarning("Visualisation Tool", message="Entered a non-hexadecimal value")
            return False

    def num_check(self, controller, encrypt):
        input = self.controller.shared_data["AES_input"].get()
        key_1 = self.controller.shared_data["AES_key_1"].get()
        key_2 = self.controller.shared_data["AES_key_2"].get()

        if len(input) != 32 or len(key_1) != 32 or len(key_2) != 32:
            messagebox.showwarning("Visualisation Tool", "Inputs are not the right length of 32 bytes")
            return False

        if encrypt:
            controller.show_frame("AES_Encrypt_Page_1")
        if not encrypt:
            controller.show_frame("AES_Decrypt_Page_1")


class AES_Encrypt_Page_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Visualisation of Plaintext and Keys",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_txt = "The plaintext and keys are shown in the arrangement seen below, in 4x4 tables.\n" \
                          "The plaintext is known as the State, once the AES algorithms operations are performed on it."
        explanation_label = Label(self, text=explanation_txt, font=("Arial", 14))
        explanation_label.pack(ipady=20)

        plaintext_label = Label(self)
        plaintext_label.pack()
        self.plaintext_label = plaintext_label

        key_1_label = Label(self)
        key_1_label.pack()
        self.key_1_label = key_1_label

        key_2_label = Label(self)
        key_2_label.pack()
        self.key_2_label = key_2_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("AES_Encrypt_Page_2"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        plaintext = self.controller.shared_data["AES_input"].get()
        key_1 = self.controller.shared_data["AES_key_1"].get()
        key_2 = self.controller.shared_data["AES_key_2"].get()

        plaintext = aes_logic.make_table(plaintext)
        key_1 = aes_logic.make_table(key_1)
        key_2 = aes_logic.make_table(key_2)

        ptxt = "Plaintext: \n" + str(plaintext[0]) + ',\n' + str(plaintext[1]) + ',\n' + \
               str(plaintext[2]) + ',\n' + str(plaintext[3]) + '\n'

        self.plaintext_label = Label(self, text=ptxt, font=("Calibri", 15))
        self.plaintext_label.pack(side='left', ipadx=120)

        k_1 = "Key 1: \n" + str(key_1[0]) + ',\n' + str(key_1[1]) + ',\n' + \
              str(key_1[2]) + ',\n' + str(key_1[3]) + '\n'
        self.key_1_label = Label(self, text=k_1, font=("Calibri", 15))
        self.key_1_label.pack(side='left', ipadx=120)

        k_2 = "Key 2: \n" + str(key_2[0]) + ',\n' + str(key_2[1]) + ',\n' + \
              str(key_2[2]) + ',\n' + str(key_2[3]) + '\n'
        self.key_2_label = Label(self, text=k_2, font=("Calibri", 15))
        self.key_2_label.pack(side='left', ipadx=120)

        self.controller.shared_data["AES_plaintext_table"] = plaintext
        self.controller.shared_data["AES_key_1_table"] = key_1
        self.controller.shared_data["AES_key_2_table"] = key_2


class AES_Encrypt_Page_2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Plaintext XORed with Key 1", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nThe First step is XOR the plaintext with the first key"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack(ipady=10)

        plaintext_xor_key_label = Label(self)
        plaintext_xor_key_label.pack()
        self.plaintext_xor_key_label = plaintext_xor_key_label

        result_label = Label(self, bg='orange')
        result_label.pack()
        self.result_label = result_label

        next_button = Button(self, text="NEXT", command=lambda: self.controller.show_frame("AES_Encrypt_Page_3"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        plaintext = self.controller.shared_data["AES_plaintext_table"]
        key_1 = self.controller.shared_data["AES_key_1_table"]

        text = "Plaintext:" + '         ' + "Key 1:" + '\n' + \
               str(plaintext[0]) + '         ' + str(key_1[0]) + '\n' + \
               str(plaintext[1]) + '  ⊕     ' + str(key_1[1]) + '\n' + \
               str(plaintext[2]) + '         ' + str(key_1[2]) + '\n' + \
               str(plaintext[3]) + '         ' + str(key_1[3]) + '\n'

        updated_plaintext_xor_key_label = Label(self.plaintext_xor_key_label, text=text, font=("Calibri", 15))
        updated_plaintext_xor_key_label.pack()

        result = aes_logic.add_round_key(plaintext, key_1)
        result_text = "Result: \n" + str(result[0]) + ',\n' + str(result[1]) + ',\n' + \
                      str(result[2]) + ',\n' + str(result[3]) + '\n'

        updated_result_label = Label(self.result_label, text=result_text, font=("Calibri", 15))
        updated_result_label.pack()


class AES_Encrypt_Page_3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Substitution of Bytes", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.grid(column=0, columnspan=3, row=0, ipadx=450, ipady=5)

        explanation_text = "Each byte in the State acts as the coordinates for the value in the lookup table that " \
                           "it will be substituted with."
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.grid(column=0, row=1, columnspan=3)

        plaintext_label = Label(self)
        plaintext_label.grid(column=0, row=2)
        self.plaintext_label = plaintext_label

        plaintext_bytes = Label(self)
        plaintext_bytes.grid(column=0, row=3)
        self.plaintext_bytes = plaintext_bytes

        lookup_bytes = Label(self)
        lookup_bytes.grid(column=1, row=3)
        self.lookup_bytes = lookup_bytes

        result_bytes = Label(self)
        result_bytes.grid(column=2, row=3)
        self.result_bytes = result_bytes

        result_label = Label(self)
        result_label.grid(column=2, row=2)
        self.result_label = result_label

        s_box = ["[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76]",
                 "[0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0]",
                 "[0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15]",
                 "[0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75]",
                 "[0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84]",
                 "[0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF]",
                 "[0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8]",
                 "[0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2]",
                 "[0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73]",
                 "[0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB]",
                 "[0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79]",
                 "[0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08]",
                 "[0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A]",
                 "[0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E]",
                 "[0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF]",
                 "[0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]"]
        lookup_text = ""
        for i in range(0, 16):
            lookup_text += (str(i) + ' ' + s_box[i].lower()) + '\n'
        lookup_table_label = Label(self, text=lookup_text, font=("Calibri", 11))
        lookup_table_label.grid(row=4, column=0, columnspan=3)

        next_button = Button(self, text="NEXT", command=lambda: self.controller.show_frame("AES_Encrypt_Page_4"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.grid(row=5, column=1)

    def updateText(self):
        plaintext = self.controller.shared_data["AES_plaintext_table"]
        first_bytes = plaintext[0][0]

        ptxt = "Plaintext: \n" + str(plaintext[0]) + ',\n' + str(plaintext[1]) + ',\n' + \
               str(plaintext[2]) + ',\n' + str(plaintext[3])

        updated_plaintext_label = Label(self.plaintext_label, text=ptxt, font=("Calibri", 15))
        updated_plaintext_label.grid(column=0, row=2)

        ptxt_bytes = "Plaintext value at plaintext[0,0]: " + str(first_bytes)
        updated_plaintext_bytes = Label(self.plaintext_bytes, text=ptxt_bytes, font=("Calibri", 14))
        updated_plaintext_bytes.grid(column=0, row=3)

        s_box = [[0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
                 [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
                 [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
                 [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
                 [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
                 [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
                 [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
                 [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
                 [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
                 [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
                 [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
                 [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
                 [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
                 [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
                 [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
                 [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]]

        lookup_bytes_text = "Lookup value at lookup[" + str(first_bytes[0]) + ", " + str(first_bytes[1]) + "]" + \
                            ":" + hex(s_box[int(first_bytes[0], base=16)][int(first_bytes[1], base=16)])
        updated_lookup_bytes = Label(self.lookup_bytes, text=lookup_bytes_text, font=("Calibri", 14))
        updated_lookup_bytes.grid(column=2, row=3)

        result = aes_logic.s_box(plaintext)
        result_text = "Result: \n" + str(result[0]) + ',\n' + str(result[1]) + ',\n' + \
                      str(result[2]) + ',\n' + str(result[3])
        updated_result_label = Label(self.result_label, text=result_text, font=("Calibri", 15))
        updated_result_label.grid(column=2, row=2)

        result_bytes_text = "Substituted plaintext at [0,0]: " + result[0][0]
        updated_result_bytes = Label(self.result_bytes, text=result_bytes_text, font=("Calibri", 14))
        updated_result_bytes.grid(column=2, row=3)


class AES_Encrypt_Page_4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Shifting of Rows", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "\nThe rows of the plaintext are shifted a certain amount of spaces to the left depending " \
                           "on the row.\nThe First Row is not shifted.\n The Second Row is shifted one space to the " \
                           "left.\nThe Third Row is shifted two spaces to the left.\n And the Final Row is shifted " \
                           "three spaces to the left.\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.pack()

        plaintext_label = Label(self)
        plaintext_label.pack()
        self.plaintext_label = plaintext_label

        result_label = Label(self, bg='orange')
        result_label.pack()
        self.result_label = result_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("AES_Encrypt_Page_5"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        plaintext = self.controller.shared_data["AES_plaintext_table"]
        ptxt = "Plaintext: \n" + str(plaintext[0]) + ',\n' + str(plaintext[1]) + ',\n' + \
               str(plaintext[2]) + ',\n' + str(plaintext[3]) + '\n'
        updated_plaintext_label = Label(self.plaintext_label, text=ptxt, font=("Calibri", 15))
        updated_plaintext_label.pack()

        result = aes_logic.shift_rows(plaintext)
        result_text = "Result: \n" + str(result[0]) + ',\n' + str(result[1]) + ',\n' + \
                      str(result[2]) + ',\n' + str(result[3]) + '\n'
        updated_result_label = Label(self.result_label, text=result_text, font=("Calibri", 15))
        updated_result_label.pack()

        self.controller.shared_data["AES_plaintext_table"] = result


class AES_Encrypt_Page_5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Mixing of Columns", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.grid(columnspan=2, row=0, ipadx=500, ipady=10)

        explanation_text = "Each column in the state is multiplied, over GF(28), by the matrix seen below to produce " \
                           "the column it gets substituted with.\n" \
                           "In the actual AES cipher, this does not happen on the last round"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 14))
        explanation_label.grid(column=0, row=1, columnspan=2)

        plaintext_label = Label(self)
        plaintext_label.grid(column=0, row=2)
        self.plaintext_label = plaintext_label

        result_label = Label(self, bg="orange")
        result_label.grid(column=1, row=2)
        self.result_label = result_label

        explanation_label = Label(self, text="Each column is multiplied by this matrix:", font=("Arial", 10))
        explanation_label.grid(column=0, row=3)

        example_label = Label(self)
        example_label.grid(column=0, row=4)
        self.example_label = example_label

        # matrix = [[2, 3, 1, 1],
        #           [1, 2, 3, 1],
        #           [1, 1, 2, 3],
        #           [3, 1, 1, 2]]
        # matrix_text = str(matrix[0]) + '\n' + str(matrix[1]) + '\n' + str(matrix[2]) + '\n' + str(matrix[3])
        # matrix_label = Label(self, text=matrix_text, font=("Arial", 12))
        # matrix_label.grid(column=1, row=3)
        explanation_result_label = Label(self, text="To produce the new column in the resulting state:",
                                         font=("Arial", 10))
        explanation_result_label.grid(column=1, row=3)

        answer_label = Label(self)
        answer_label.grid(column=1, row=4)
        self.answer_label = answer_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("AES_Encrypt_Page_6"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.grid(column=1, row=5)

    def updateText(self):
        plaintext = self.controller.shared_data["AES_plaintext_table"]
        ptxt = "Plaintext: \n" + str(plaintext[0]) + ',\n' + str(plaintext[1]) + ',\n' + \
               str(plaintext[2]) + ',\n' + str(plaintext[3]) + '\n'
        updated_plaintext_label = Label(self.plaintext_label, text=ptxt, font=("Arial", 15))
        updated_plaintext_label.grid(column=0, row=2)

        result = aes_logic.mix_columns(plaintext)
        result_text = "Result: \n" + str(result[0]) + ',\n' + str(result[1]) + ',\n' + \
                      str(result[2]) + ',\n' + str(result[3]) + '\n'
        updated_result_label = Label(self.result_label, text=result_text, font=("Arial", 15))
        updated_result_label.grid(column=1, row=2)

        plaintext = aes_logic.inv_mix_columns(plaintext)

        matrix = [[2, 3, 1, 1],
                  [1, 2, 3, 1],
                  [1, 1, 2, 3],
                  [3, 1, 1, 2]]

        example_text = str(plaintext[0][0]) + '    ' + str(matrix[0]) + '\n' + \
                       str(plaintext[1][0]) + ' *  ' + str(matrix[1]) + '\n' + \
                       str(plaintext[2][0]) + '    ' + str(matrix[2]) + '\n' + \
                       str(plaintext[3][0]) + '    ' + str(matrix[3])

        # example_text = str(plaintext[0][0]) + '    \n' + str(plaintext[1][0]) + '   *\n' +\
        #                str(plaintext[2][0]) + '    \n' + str(plaintext[3][0]) + '    '
        updated_example_label = Label(self.example_label, text=example_text, font=("Arial", 12))
        updated_example_label.grid(column=0, row=4)

        result = aes_logic.mix_columns(plaintext)
        answer_text = str(result[0][0]) + "\n" + str(result[1][0]) + "\n" + str(result[2][0]) + "\n" + \
                      str(result[3][0]) + "\n"
        updated_answer_label = Label(self.answer_label, text=answer_text, font=("Arial", 12))
        updated_answer_label.grid(column=1, row=4)


class AES_Encrypt_Page_6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Plaintext XORed with Key 2", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        plaintext_xor_key_label = Label(self)
        plaintext_xor_key_label.pack()
        self.plaintext_xor_key_label = plaintext_xor_key_label

        result_label = Label(self)
        result_label.pack()
        self.result_label = result_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("AES_Encrypt_Page_7"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        plaintext = self.controller.shared_data["AES_plaintext_table"]
        key_2 = self.controller.shared_data["AES_key_2_table"]

        text = "Plaintext:" + '         ' + "Key 2:" + '\n' + \
               str(plaintext[0]) + '         ' + str(key_2[0]) + '\n' + \
               str(plaintext[1]) + '  ⊕     ' + str(key_2[1]) + '\n' + \
               str(plaintext[2]) + '         ' + str(key_2[2]) + '\n' + \
               str(plaintext[3]) + '         ' + str(key_2[3]) + '\n'

        updated_plaintext_xor_key_label = Label(self.plaintext_xor_key_label, text=text, font=("Arial", 15))
        updated_plaintext_xor_key_label.pack()

        result = aes_logic.add_round_key(plaintext, key_2)
        result_text = "Result: \n" + str(result[0]) + ',\n' + str(result[1]) + ',\n' + \
                      str(result[2]) + ',\n' + str(result[3]) + '\n'

        updated_result_label = Label(self.result_label, text=result_text, font=("Arial", 15))
        updated_result_label.pack()

        self.controller.shared_data["AES_plaintext_table"] = result


class AES_Encrypt_Page_7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Ciphertext Result", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        ciphertext_table_label = Label(self)
        ciphertext_table_label.pack()
        self.ciphertext_table_label = ciphertext_table_label

        ciphertext_label = Label(self, bg='orange')
        ciphertext_label.pack()
        self.ciphertext_label = ciphertext_label

    def updateText(self):
        ciphertext_table = self.controller.shared_data["AES_plaintext_table"]
        ctxt = "Ciphertext: \n" + str(ciphertext_table[0]) + ',\n' + str(ciphertext_table[1]) + ',\n' + \
               str(ciphertext_table[2]) + ',\n' + str(ciphertext_table[3]) + '\n'
        updated_ciphertext_table_label = Label(self.ciphertext_table_label, text=ctxt, font=("Arial", 15))
        updated_ciphertext_table_label.pack()

        ciphertext = ""
        for rows in range(0, 4):
            for columns in range(0, 4):
                ciphertext += str(ciphertext_table[columns][rows])
        ciphertext = '0x' + ciphertext
        updated_ciphertext_label = Label(self.ciphertext_label, text=ciphertext, font=("Arial", 20))
        updated_ciphertext_label.pack()


class AES_Decrypt_Page_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Visualisation of Ciphertext and Keys",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_txt = "arrangement =\n [[b0, b4, b8, b12],\n[b1, b5, b9, b13],\n" \
                          "[b2, b6, b10, b14],\n[b3, b7, b11, b15]"
        explanation_label = Label(self, text=explanation_txt, font=("Arial", 12))
        explanation_label.pack()

        ciphertext_label = Label(self)
        ciphertext_label.pack()
        self.ciphertext_label = ciphertext_label

        key_1_label = Label(self)
        key_1_label.pack()
        self.key_1_label = key_1_label

        key_2_label = Label(self)
        key_2_label.pack()
        self.key_2_label = key_2_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("AES_Decrypt_Page_2"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        ciphertext = self.controller.shared_data["AES_input"].get()
        key_1 = self.controller.shared_data["AES_key_1"].get()
        key_2 = self.controller.shared_data["AES_key_2"].get()

        ciphertext = aes_logic.make_table(ciphertext)
        key_1 = aes_logic.make_table(key_1)
        key_2 = aes_logic.make_table(key_2)

        ctxt = "Ciphertext: \n" + str(ciphertext[0]) + ',\n' + str(ciphertext[1]) + ',\n' + \
               str(ciphertext[2]) + ',\n' + str(ciphertext[3]) + '\n'

        self.ciphertext_label = Label(self, text=ctxt, font=("Arial", 15))
        self.ciphertext_label.pack(side='left', ipadx=120)

        k_1 = "Key 1: \n" + str(key_1[0]) + ',\n' + str(key_1[1]) + ',\n' + \
              str(key_1[2]) + ',\n' + str(key_1[3]) + '\n'
        self.key_1_label = Label(self, text=k_1, font=("Arial", 15))
        self.key_1_label.pack(side='left', ipadx=120)

        k_2 = "Key 2: \n" + str(key_2[0]) + ',\n' + str(key_2[1]) + ',\n' + \
              str(key_2[2]) + ',\n' + str(key_2[3]) + '\n'
        self.key_2_label = Label(self, text=k_2, font=("Arial", 15))
        self.key_2_label.pack(side='left', ipadx=120)

        self.controller.shared_data["AES_ciphertext_table"] = ciphertext
        self.controller.shared_data["AES_key_1_table"] = key_1
        self.controller.shared_data["AES_key_2_table"] = key_2


class AES_Decrypt_Page_2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Ciphertext XORed with Key 2",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        ciphertext_xor_key_label = Label(self)
        ciphertext_xor_key_label.pack()
        self.ciphertext_xor_key_label = ciphertext_xor_key_label

        result_label = Label(self)
        result_label.pack()
        self.result_label = result_label

        next_button = Button(self, text="NEXT", command=lambda: self.controller.show_frame("AES_Decrypt_Page_3"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        ciphertext = self.controller.shared_data["AES_ciphertext_table"]
        key_2 = self.controller.shared_data["AES_key_2_table"]

        text = "ciphertext:" + '         ' + "Key 2:" + '\n' + \
               str(ciphertext[0]) + '         ' + str(key_2[0]) + '\n' + \
               str(ciphertext[1]) + '  ⊕     ' + str(key_2[1]) + '\n' + \
               str(ciphertext[2]) + '         ' + str(key_2[2]) + '\n' + \
               str(ciphertext[3]) + '         ' + str(key_2[3]) + '\n'

        updated_ciphertext_xor_key_label = Label(self.ciphertext_xor_key_label, text=text, font=("Arial", 15))
        updated_ciphertext_xor_key_label.pack()

        result = aes_logic.add_round_key(ciphertext, key_2)
        result_text = "Result: \n" + str(result[0]) + ',\n' + str(result[1]) + ',\n' + \
                      str(result[2]) + ',\n' + str(result[3]) + '\n'

        updated_result_label = Label(self.result_label, text=result_text, font=("Arial", 15))
        updated_result_label.pack()


class AES_Decrypt_Page_3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Invert the Mixing of Columns", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.grid(columnspan=3, row=0, ipadx=400, ipady=10)

        ciphertext_label = Label(self)
        ciphertext_label.grid(column=0, row=1)
        self.ciphertext_label = ciphertext_label

        result_label = Label(self, bg="orange")
        result_label.grid(column=2, row=1)
        self.result_label = result_label

        explanation_label = Label(self, text="Each column is multiplied by this matrix:", font=("Arial", 10))
        explanation_label.grid(column=0, row=2)

        example_label = Label(self)
        example_label.grid(column=0, row=3)
        self.example_label = example_label

        explanation_result_label = Label(self, text="To produce the new column in the resulting state:",
                                         font=("Arial", 10))
        explanation_result_label.grid(column=1, row=2)

        answer_label = Label(self)
        answer_label.grid(column=1, row=3)
        self.answer_label = answer_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("AES_Decrypt_Page_4"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.grid(column=1, row=4, pady=210)

    def updateText(self):
        ciphertext = self.controller.shared_data["AES_ciphertext_table"]
        ctxt = "ciphertext: \n" + str(ciphertext[0]) + ',\n' + str(ciphertext[1]) + ',\n' + \
               str(ciphertext[2]) + ',\n' + str(ciphertext[3]) + '\n'
        updated_ciphertext_label = Label(self.ciphertext_label, text=ctxt, font=("Arial", 15))
        updated_ciphertext_label.grid(column=0, row=1)

        result = aes_logic.inv_mix_columns(ciphertext)
        result_text = "Result: \n" + str(result[0]) + ',\n' + str(result[1]) + ',\n' + \
                      str(result[2]) + ',\n' + str(result[3]) + '\n'
        updated_result_label = Label(self.result_label, text=result_text, font=("Arial", 15))
        updated_result_label.grid(column=1, row=1)

        ciphertext = aes_logic.inv_mix_columns(ciphertext)

        matrix = [[2, 3, 1, 1],
                  [1, 2, 3, 1],
                  [1, 1, 2, 3],
                  [3, 1, 1, 2]]

        example_text = str(ciphertext[0][0]) + '    ' + str(matrix[0]) + '\n' + \
                       str(ciphertext[1][0]) + ' *  ' + str(matrix[1]) + '\n' + \
                       str(ciphertext[2][0]) + '    ' + str(matrix[2]) + '\n' + \
                       str(ciphertext[3][0]) + '    ' + str(matrix[3])

        updated_example_label = Label(self.example_label, text=example_text, font=("Arial", 12))
        updated_example_label.grid(column=0, row=3)

        result = aes_logic.mix_columns(ciphertext)
        answer_text = str(result[0][0]) + "\n" + str(result[1][0]) + "\n" + str(result[2][0]) + "\n" + \
                      str(result[3][0]) + "\n"
        updated_answer_label = Label(self.answer_label, text=answer_text, font=("Arial", 12))
        updated_answer_label.grid(column=1, row=3)


class AES_Decrypt_Page_4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Invert the Shifting of Rows",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "The rows of the ciphertext are shifted a certain amount of spaces to the right depending " \
                           "on the row.\nThe First Row is not shifted.\n The Second Row is shifted one space to the " \
                           "right.\nThe Third Row is shifted two spaces to the right\n. And the Final Row is shifted " \
                           "3 spaces to the right.\n"
        explanation_label = Label(self, text=explanation_text, font=("Arial", 10))
        explanation_label.pack()

        ciphertext_label = Label(self)
        ciphertext_label.pack()
        self.ciphertext_label = ciphertext_label

        result_label = Label(self)
        result_label.pack()
        self.result_label = result_label

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("AES_Decrypt_Page_5"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        ciphertext = self.controller.shared_data["AES_ciphertext_table"]
        ctxt = "Ciphertext: \n" + str(ciphertext[0]) + ',\n' + str(ciphertext[1]) + ',\n' + \
               str(ciphertext[2]) + ',\n' + str(ciphertext[3]) + '\n'
        updated_ciphertext_label = Label(self.ciphertext_label, text=ctxt, font=("Arial", 15))
        updated_ciphertext_label.pack()

        result = aes_logic.inv_shift_rows(ciphertext)
        result_text = "Result: \n" + str(result[0]) + ',\n' + str(result[1]) + ',\n' + \
                      str(result[2]) + ',\n' + str(result[3]) + '\n'
        updated_result_label = Label(self.result_label, text=result_text, font=("Arial", 15))
        updated_result_label.pack()

        self.controller.shared_data["AES_ciphertext_table"] = result


class AES_Decrypt_Page_5(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Invert the Substitution of Bytes", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.grid(column=0, columnspan=3, row=0, ipadx=400, ipady=10)

        explanation_text = "Each byte in the ciphertext is substituted with another one found in the lookup table\n" \
                           "The leftmost digit of the hexadecimal value corresponds to the vertical axis of " \
                           "the lookup table and the rightmost digit corresponds to the horizontal axis."
        explanation_label = Label(self, text=explanation_text, font=("Arial", 10))
        explanation_label.grid(column=0, row=1, columnspan=3)

        ciphertext_label = Label(self)
        ciphertext_label.grid(column=0, row=2)
        self.ciphertext_label = ciphertext_label

        ciphertext_bytes = Label(self)
        ciphertext_bytes.grid(column=0, row=3)
        self.ciphertext_bytes = ciphertext_bytes

        lookup_bytes = Label(self)
        lookup_bytes.grid(column=1, row=3)
        self.lookup_bytes = lookup_bytes

        result_bytes = Label(self)
        result_bytes.grid(column=2, row=3)
        self.result_bytes = result_bytes

        result_label = Label(self)
        result_label.grid(column=2, row=2)
        self.result_label = result_label

        inverted_s_box = [
            "[0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB]",
            "[0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB]",
            "[0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E]",
            "[0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25]",
            "[0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92]",
            "[0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84]",
            "[0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06]",
            "[0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B]",
            "[0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73]",
            "[0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E]",
            "[0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B]",
            "[0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4]",
            "[0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F]",
            "[0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF]",
            "[0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61]",
            "[0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]"]
        lookup_text = ""
        for i in range(0, 16):
            lookup_text += (str(i) + ' ' + inverted_s_box[i].lower()) + '\n'
        lookup_table_label = Label(self, text=lookup_text, font=("Arial", 10))
        lookup_table_label.grid(row=4, column=0, columnspan=3)

        next_button = Button(self, text="NEXT", command=lambda: self.controller.show_frame("AES_Decrypt_Page_6"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.grid(row=5, column=1, pady=15)

    def updateText(self):
        ciphertext = self.controller.shared_data["AES_ciphertext_table"]
        first_bytes = ciphertext[0][0]

        ctxt = "Ciphertext: \n" + str(ciphertext[0]) + ',\n' + str(ciphertext[1]) + ',\n' + \
               str(ciphertext[2]) + ',\n' + str(ciphertext[3])

        updated_ciphertext_label = Label(self.ciphertext_label, text=ctxt, font=("Arial", 15))
        updated_ciphertext_label.grid(column=0, row=2)

        ctxt_bytes = "Ciphertext value at plaintext[0,0]: " + str(first_bytes)
        updated_ciphertext_bytes = Label(self.ciphertext_bytes, text=ctxt_bytes, font=("Arial", 12))
        updated_ciphertext_bytes.grid(column=0, row=3)

        inverted_s_box = [
            [0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB],
            [0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB],
            [0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E],
            [0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25],
            [0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92],
            [0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84],
            [0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06],
            [0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B],
            [0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73],
            [0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E],
            [0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B],
            [0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4],
            [0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F],
            [0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF],
            [0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61],
            [0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D]]

        lookup_bytes_text = "Lookup value at lookup[" + str(first_bytes[0]) + ", " + str(first_bytes[1]) + "]" + \
                            ":" + hex(inverted_s_box[int(first_bytes[0], base=16)][int(first_bytes[1], base=16)])
        updated_lookup_bytes = Label(self.lookup_bytes, text=lookup_bytes_text, font=("Arial", 12))
        updated_lookup_bytes.grid(column=2, row=3)

        result = aes_logic.inv_s_box(ciphertext)
        result_text = "Result: \n" + str(result[0]) + ',\n' + str(result[1]) + ',\n' + \
                      str(result[2]) + ',\n' + str(result[3])
        updated_result_label = Label(self.result_label, text=result_text, font=("Arial", 15))
        updated_result_label.grid(column=2, row=2)

        result_bytes_text = "Substituted plaintext at [0,0]: " + result[0][0]
        updated_result_bytes = Label(self.result_bytes, text=result_bytes_text, font=("Arial", 12))
        updated_result_bytes.grid(column=2, row=3)


class AES_Decrypt_Page_6(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Ciphertext XORed with Key 1",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        ciphertext_xor_key_label = Label(self)
        ciphertext_xor_key_label.pack()
        self.ciphertext_xor_key_label = ciphertext_xor_key_label

        result_label = Label(self)
        result_label.pack()
        self.result_label = result_label

        next_button = Button(self, text="NEXT", command=lambda: self.controller.show_frame("AES_Decrypt_Page_7"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side=BOTTOM)

    def updateText(self):
        ciphertext = self.controller.shared_data["AES_ciphertext_table"]
        key_1 = self.controller.shared_data["AES_key_1_table"]

        text = "ciphertext:" + '         ' + "Key 1:" + '\n' + \
               str(ciphertext[0]) + '         ' + str(key_1[0]) + '\n' + \
               str(ciphertext[1]) + '  ⊕     ' + str(key_1[1]) + '\n' + \
               str(ciphertext[2]) + '         ' + str(key_1[2]) + '\n' + \
               str(ciphertext[3]) + '         ' + str(key_1[3]) + '\n'

        updated_ciphertext_xor_key_label = Label(self.ciphertext_xor_key_label, text=text, font=("Arial", 15))
        updated_ciphertext_xor_key_label.pack()

        result = aes_logic.add_round_key(ciphertext, key_1)
        result_text = "Result: \n" + str(result[0]) + ',\n' + str(result[1]) + ',\n' + \
                      str(result[2]) + ',\n' + str(result[3]) + '\n'

        updated_result_label = Label(self.result_label, text=result_text, font=("Arial", 15))
        updated_result_label.pack()


class AES_Decrypt_Page_7(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Plaintext Result", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        ciphertext_table_label = Label(self)
        ciphertext_table_label.pack()
        self.ciphertext_table_label = ciphertext_table_label

        plaintext_label = Label(self, bg='orange')
        plaintext_label.pack()
        self.plaintext_label = plaintext_label

    def updateText(self):
        ciphertext_table = self.controller.shared_data["AES_ciphertext_table"]
        ptxt = "Plaintext: \n" + str(ciphertext_table[0]) + ',\n' + str(ciphertext_table[1]) + ',\n' + \
               str(ciphertext_table[2]) + ',\n' + str(ciphertext_table[3]) + '\n'
        updated_ciphertext_table_label = Label(self.ciphertext_table_label, text=ptxt, font=("Arial", 15))
        updated_ciphertext_table_label.pack()

        plaintext = ""
        for rows in range(0, 4):
            for columns in range(0, 4):
                plaintext += str(ciphertext_table[columns][rows])
        plaintext = '0x' + plaintext
        updated_ciphertext_label = Label(self.plaintext_label, text=plaintext, font=("Arial", 20))
        updated_ciphertext_label.pack()


class DES_Key_Gen_Page(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        key = self.controller.shared_data["Key_gen_Key"]

        title_label = Label(self, text="DES Key Generation Page", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        input_label = Label(self, text="Input 64-Bit String:", font=("Arial", 20), fg="black")
        input_label.pack(expand=True)

        input_entry = Entry(self, textvariable=key, bg='white', font=("Arial", 10))
        input_entry.pack(ipadx=155, ipady=10, expand=True)
        input_entry.focus()
        self.input_entry = input_entry
        input_reg = self.register(self.input_callback)
        input_entry.config(validate="key", validatecommand=(input_reg, '%P'))

        random_input = Button(self, text="Random", bg='#cf3030', fg="white", font=("Arial", 10),
                              command=lambda: self.make_random())
        random_input.pack(ipadx=20, ipady=10, expand=True, fill="none")

        generate_button = Button(self, text="Generate", font=("Arial", 20), bg="#e88a1a", fg="white",
                                 command=lambda: self.num_check(controller))
        generate_button.pack(ipadx=10, ipady=10, expand=True, fill="none", side=LEFT)

    def updateText(self):
        pass

    def make_random(self):
        random_text = ""
        for x in range(0, 64):
            random_text += str(random.randint(0, 1))
        self.input_entry.delete(0, END)
        self.input_entry.insert(0, random_text)

    def input_callback(self, input):
        if len(input) > 64:
            messagebox.showwarning("Visualisation Tool", message="Reached 64 bits\nMessage too long")
            return False
        elif input.isdigit() or input == "":
            if int(input[len(input) - 1]) > 1:
                messagebox.showwarning("Visualisation Tool", message="Can only enter digits: 0, 1")
                return False
            return True
        else:
            messagebox.showwarning("Visualisation Tool", message="Can only enter digits: 0, 1")
            return False

    def num_check(self, controller):
        key = self.controller.shared_data["Key_gen_Key"].get()

        if len(key) != 64:
            messagebox.showwarning("Visualisation Tool", "Check input length.\n Input must be 64 bits")
            return False

        self.controller.shared_data["Key_gen_original"] = key
        controller.show_frame("DES_Key_Gen_Page_1")


class DES_Key_Gen_Page_1(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Initial Permutation", font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

        explanation_text = "Due to the permutation order shown below, the length of the key shrinks to be 56 bits " \
                           "long as every eighth bit was a parity bit."
        explanation_label = Label(self, text=explanation_text, font=("Arial", 10))
        explanation_label.pack()

        permutation_label = Label(self, bg="orange")
        permutation_label.pack(expand=True)
        self.permutation_label = permutation_label

        permutation_order = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3,
                             60, 52, 44, 36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45,
                             37, 29, 21, 13, 5, 28, 20, 12, 4]
        permutation_order_label = Label(self, text=("Permutation Order:\n" + str(permutation_order)),
                                        font=("Arial", 10))
        permutation_order_label.pack(expand=True)

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Key_Gen_Page_2"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.pack(side='bottom')

    def updateText(self):
        key = self.controller.shared_data["Key_gen_Key"].get()
        permuted_key = des_key.permutation_order_1(list(key))

        updated_label = Label(self.permutation_label, text=(key + "\n→\n" + ''.join(permuted_key)),
                              font=("Arial", 10))
        updated_label.pack(expand=True, side=TOP)
        self.controller.shared_data["Key_gen_key"] = permuted_key


class DES_Key_Gen_Page_2(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Round N: Shifting of Left and Right Side",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.grid(row=0, column=0, columnspan=3, ipadx=350, ipady=10)

        explanation_text = "At the beginning of each round the key is split in half, and each side is shifted either " \
                           "once or twice to the left, depending on the round."
        explanation_label = Label(self, text=explanation_text, font=("Arial", 10))
        explanation_label.grid(row=1, column=0, columnspan=3, pady=25)

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Key_Gen_Page_3"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.grid(row=5, column=1, pady=215)

    def updateText(self):
        key = self.controller.shared_data["Key_gen_Key"].get()
        left_side = key[:28]
        right_side = key[28:]

        updated_original_label = Label(self, text="Permuted Key:\n" + key, font=("Arial", 10))
        updated_original_label.grid(row=2, column=0, columnspan=3, pady=20)

        updated_left_side_label = Label(self, text="Left Side:\n" + left_side, font=("Arial", 10))
        updated_left_side_label.grid(row=3, column=0)

        updated_right_side_label = Label(self, text="Right Side:\n" + right_side, font=("Arial", 10))
        updated_right_side_label.grid(row=3, column=2)

        shifted_left = list(des_key.left_shift(left_side))
        shifted_right = list(des_key.left_shift(right_side))

        updated_left_side_shift_label = Label(self, text="Shifted Left Side:\n" + (''.join(shifted_left)),
                                              font=("Arial", 10))
        updated_left_side_shift_label.grid(row=4, column=0, pady=20)

        updated_right_side_shift_label = Label(self, text="Shifted Right Side:\n" + (''.join(shifted_right)),
                                               font=("Arial", 10))
        updated_right_side_shift_label.grid(row=4, column=2, pady=20)

        self.controller.shared_data["Key_gen_left"] = shifted_left
        self.controller.shared_data["Key_gen_right"] = shifted_right


class DES_Key_Gen_Page_3(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Round N: Combination and Permutation of Left and Right Side",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.grid(row=0, column=0, columnspan=3, ipadx=160, ipady=10)

        explanation_text = "After combining the left and right side together, they are permuted once again. This " \
                           "permutation shrinks the key even more to have a length of 48 bits.\nBy repeating this " \
                           "step and the previous one, new round keys are generated for the DES cipher."
        explanation_label = Label(self, text=explanation_text, font=("Arial", 10))
        explanation_label.grid(row=1, column=0, columnspan=3)

        permutation_order = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41,
                             52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
        permutation_order_label = Label(self, text="Permutation Order:\n" + str(permutation_order), font=("Arial", 10))
        permutation_order_label.grid(row=5, column=0, columnspan=3, ipady=137)

        next_button = Button(self, text="NEXT", command=lambda: controller.show_frame("DES_Key_Gen_Page_4"),
                             font=("Arial", 10), bg="#cf3030", fg="white")
        next_button.grid(row=6, column=1)

    def updateText(self):
        left_side = self.controller.shared_data["Key_gen_left"]
        right_side = self.controller.shared_data["Key_gen_right"]

        key = left_side + right_side
        permuted_key = des_key.combine_left_and_right(list(left_side), list(right_side))

        left_side_label = Label(self, text="Left Side:\n" + (''.join(left_side)), font=("Arial", 10))
        left_side_label.grid(row=2, column=0, ipady=10)

        right_side_label = Label(self, text="Right Side:\n" + (''.join(right_side)), font=("Arial", 10))
        right_side_label.grid(row=2, column=2)

        result_text = "Result:\n" + ''.join(key) + "\n->\n" + ''.join(permuted_key)
        result_label = Label(self, text=result_text, font=("Arial", 10))
        result_label.grid(row=3, column=1)

        self.controller.shared_data["Key_gen_Key"] = permuted_key


class DES_Key_Gen_Page_4(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller

        title_label = Label(self, text="Results",
                            font=("Arial", 25), bg="#cf3030", fg="white")
        title_label.pack(fill='x', ipady=10)

    def updateText(self):
        original = self.controller.shared_data["Key_gen_original"]
        key = self.controller.shared_data["Key_gen_Key"]

        original_text = "Original Key: " + original
        original_label = Label(self, text=original_text, font=("Arial", 10))
        original_label.pack(ipady=10)

        round_1_text = "Round 1: " + ''.join(key)
        round_1_label = Label(self, text=round_1_text, font=("Arial", 10))
        round_1_label.pack(ipady=10)

        round_2_text = "Round 2: " + ''.join(des_key.gen_key(original, 2))
        round_2_label = Label(self, text=round_2_text, font=("Arial", 10))
        round_2_label.pack(ipady=10)

        round_2_text = "Round 3: " + ''.join(des_key.gen_key(original, 3))
        round_2_label = Label(self, text=round_2_text, font=("Arial", 10))
        round_2_label.pack(ipady=10)

        round_2_text = "Round 4: " + ''.join(des_key.gen_key(original, 4))
        round_2_label = Label(self, text=round_2_text, font=("Arial", 10))
        round_2_label.pack(ipady=10)

        round_2_text = "Round 5: " + ''.join(des_key.gen_key(original, 5))
        round_2_label = Label(self, text=round_2_text, font=("Arial", 10))
        round_2_label.pack(ipady=10)

        round_2_text = "Round 6: " + ''.join(des_key.gen_key(original, 6))
        round_2_label = Label(self, text=round_2_text, font=("Arial", 10))
        round_2_label.pack(ipady=10)

        round_2_text = "Round 7: " + ''.join(des_key.gen_key(original, 7))
        round_2_label = Label(self, text=round_2_text, font=("Arial", 10))
        round_2_label.pack(ipady=10)

        round_2_text = "Round 8: " + ''.join(des_key.gen_key(original, 8))
        round_2_label = Label(self, text=round_2_text, font=("Arial", 10))
        round_2_label.pack(ipady=10)

        round_2_text = "Round 9: " + ''.join(des_key.gen_key(original, 9))
        round_2_label = Label(self, text=round_2_text, font=("Arial", 10))
        round_2_label.pack(ipady=10)

        round_2_text = "Round 10: " + ''.join(des_key.gen_key(original, 10))
        round_2_label = Label(self, text=round_2_text, font=("Arial", 10))
        round_2_label.pack(ipady=10)


if __name__ == "__main__":
    app = TkinterApp()
    app.title("Visualisation tool")
    app.geometry("1200x560")

    menubar = Menu(app)
    app.config(menu=menubar)

    app.mainloop()
