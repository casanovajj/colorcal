import tkinter as tk
import calendar

# Create main window
root = tk.Tk()
root.title("Calendar 2025")
root.configure(bg="#f0f8ff")  # Light blue background

# ----- Styling -----
label_bg = "#f0f8ff"     # Match window background
entry_bg = "#ffffff"     # White entry boxes
button_bg = "#007acc"    # Bright blue button
button_fg = "#ffffff"    # White text on button
error_color = "#ff4d4d"  # Red for errors
normal_text_color = "#333333"

# ----- Widgets -----

# Year label
year_label = tk.Label(root, text='Year:', bg=label_bg, font=('Arial', 12))
year_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

# Year entry
year_entry = tk.Entry(root, bg=entry_bg, font=('Arial', 12))
year_entry.grid(row=0, column=1, padx=5, pady=5)

# Month label
month_label = tk.Label(root, text="Month:", bg=label_bg, font=('Arial', 12))
month_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

# Month entry
month_entry = tk.Entry(root, bg=entry_bg, font=('Arial', 12))
month_entry.grid(row=1, column=1, padx=5, pady=5)

# Calendar display
cal_display = tk.Label(root, font=('Courier New', 12), justify='left',
                       bg="white", fg=normal_text_color, bd=2, relief="solid", padx=10, pady=10)
cal_display.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Show calendar function
def show_calendar():
    try:
        year = int(year_entry.get())
        month = int(month_entry.get())

        if month < 1 or month > 12:
            cal_display.config(text='Invalid month! Enter a number between 1 and 12.', fg=error_color)
            return

        cal_text = calendar.month(year, month)
        cal_display.config(text=cal_text, fg=normal_text_color)  # Reset to normal color
    except ValueError:
        cal_display.config(text='Please enter valid numbers for year and month.', fg=error_color)

# Show button
show_button = tk.Button(root, text='Show Calendar', command=show_calendar,
                        bg=button_bg, fg=button_fg, font=('Arial', 12, 'bold'), padx=10, pady=5)
show_button.grid(row=2, column=0, columnspan=2, pady=10)

# Run the app
root.mainloop()
