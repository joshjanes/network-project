from collections import Counter
# Third-party libraries
import numpy as np

def main():
    file = ["afr1.txt", "cat1.txt", "cze1.txt", "dan1.txt", "dut1.txt", "eng1.txt", "fin1.txt", "fren1.txt", "ger1.txt", "hun1.txt", "ice1.txt", "lat1.txt", "nor1.txt", "pol1.txt", "port1.txt", "span1.txt", "swe1.txt", "tag1.txt"]
    langs = ["Afrikaans", "Catalan", "Czech", "Danish", "Dutch", "English", "Finnish", "French", "German", "Hungarian", "Icelandic", "Latin", "Norwegian", "Polish", "Portuguese", "Spanish", "Swedish", "Tagalog"]
    letters = "abcdefghijklmnopqrstuvwxyz���������������������������"
    #Connection weights from hidden units (rows) to output units (columns):
    bias_hidden_out = [-0.66, -0.56, -0.31, -0.10, -0.23, -0.45, -0.35, -0.17, -0.36, -0.39, -0.42, -0.23, -0.52, -0.26, -0.33, -0.19, -0.47, -0.41]
    hidden_out = [ [-0.56, -0.44, -0.04, 0.16, -0.02, -0.34, -0.56, 0.05, -0.18, -0.28, -0.40, -0.16, -0.29, -0.75, -0.24, 0.06, -0.45, -0.72],
    [0.18, -3.46, -0.35, -5.35, 1.08, 0.94, 0.60, 0.63, 1.41, 0.57, -0.11, 0.42, 3.86, 0.63, -2.42, -1.94, -0.03, -2.64],
    [-0.49, -0.40, -0.44, -0.03, -0.18, -0.37, -0.30, -0.11, -0.25, -0.44, -0.51, -0.24, -0.32, -0.56, -0.35, -0.02, -0.47, -0.41], 
    [0.61, 1.62, -1.74, 0.21, 0.17, 0.22, -0.09, 0.34, 0.17, -1.87, 0.10, 0.53, 0.36, -1.58, 1.49, 0.78, 0.17, -1.56],
    [2.53, -3.97, 1.03, -4.28, 0.21, 1.55, 1.09, -1.18, -0.25, -0.49, -1.33, 0.76, -3.53, 1.08, 1.66, 1.58, -0.43, 1.88],
    [0.77, -0.83, 0.63, -0.27, -3.35, 0.33, 0.04, 0.04, -0.52, 0.00, 0.08, 0.43, 2.82, -0.26, 0.25, -3.08, 0.39, -1.22],
    [-0.52, -0.36, 0.01, -0.20, -0.41, -0.33, -0.23, -0.16, -0.50, -0.34, -0.10, 0.02, -0.45, -0.10, -0.40, -0.15, -0.18, -0.70] ,
    [-0.41, -0.22, -1.00, 0.45, 0.96, -1.02, -0.02, -0.37, -0.15, -0.64, -1.34, -0.79, -1.16, 0.65, -0.07, 0.37, -1.38, 0.48],
    [-3.81, 2.81, 1.22, -0.06, -2.42, 0.22, 0.43, -3.17, -2.00, 0.28, 0.71, 0.20, -2.05, -1.75, 3.19, -3.23, 2.51, 1.92] ,
    [0.97, 0.71, -0.63, -0.05, -1.04, -2.50, 1.06, -1.90, 0.67, 1.43, 0.95, -0.99, 0.17, 1.10, -1.98, -4.98, 1.18, 5.09] ,
    [-0.65, -0.51, -0.04, -0.11, -0.69, -0.39, -0.21, -0.10, -0.39, -0.20, -0.15, 0.03, -0.55, -0.06, -0.23, -0.14, -0.27, -0.74], 
    [3.65, -2.56, 1.62, -3.31, -1.74, 1.28, 0.74, -1.23, 0.35, -1.42, 0.69, 1.35, -0.07, 0.40, 0.94, -4.26, -0.62, -1.18],
    [-0.24, -0.38, -0.11, -0.03, -0.33, -0.21, -0.19, -0.11, -0.22, -0.21, -0.13, 0.00, -0.31, 0.02, -0.22, 0.21, -0.13, -1.96], 
    [-0.98, -0.34, 0.40, -0.79, 0.07, -0.22, -1.10, 0.31, -0.11, 0.13, -0.24, 0.35, -0.62, 0.34, -0.10, 0.59, -1.10, -0.94], 
    [2.26, -0.59, 1.10, 2.07, -4.54, -1.01, 0.34, 0.02, -2.16, 0.66, 0.24, -0.01, 0.57, -1.56, 1.01, 0.19, 1.14, 0.53],
    [-0.22, -1.64, -0.73, 1.01, 0.70, 0.84, -1.46, 0.24, 0.32, 0.34, -2.99, -2.42, -0.02, 0.44, 0.35, 1.66, 0.67, 1.17], 
    [-0.54, -0.31, -0.35, 0.14, 0.01, -0.27, -1.85, 0.08, -0.04, -0.45, -0.20, 0.24, -0.33, -0.13, -0.22, 0.05, -0.44, -0.91], 
    [-0.42, -0.38, 0.04, -0.17, -0.71, -0.31, -0.22, -0.13, -0.62, -0.11, -0.04, 0.04, -0.42, -0.21, -0.21, 0.07, -0.03, -1.21], 
    [2.09, -1.42, -2.44, 0.88, 0.79, -0.29, -1.44, -0.23, 0.72, 1.07, 1.35, -0.93, 1.45, 0.75, -3.04, 1.05, -2.88, 1.98], 
    [-0.17, -0.28, -0.70, 0.52, -1.01, -1.56, -0.54, 0.06, -1.25, -1.14, 0.48, 0.06, -0.76, -0.30, 1.23, 0.35, -0.36, 0.77], 
    [0.75, -2.17, -1.84, -0.32, 0.08, -0.29, -1.13, -3.14, 1.07, -1.23, 1.20, 0.65, -4.30, 1.60, 2.45, 0.97, -2.05, 2.98], 
    [-0.60, -0.44, -0.23, 0.01, -0.02, -0.35, -1.06, -0.02, -0.10, -0.62, -0.36, -0.14, -0.29, -0.56, -0.13, 0.02, -0.38, -0.83], 
    [0.13, -1.11, -0.81, -2.53, -0.17, -1.69, 1.12, -0.47, 0.71, 0.57, 1.99, 0.65, -0.34, 0.49, -2.00, -2.16, -1.33, 1.67],
    [-0.62, -0.48, -0.90, 0.01, -0.40, -0.31, -0.58, -0.27, -0.26, -0.66, -0.02, -0.07, -0.50, -0.24, -0.30, -0.04, -0.29, 0.23], 
    [-2.50, 0.35, -0.55, -0.99, -2.07, 0.51, 0.53, -0.64, 2.58, -0.98, 0.78, 0.70, -4.22, -1.04, 1.25, -4.27, 1.80, 3.88], 
    [-0.55, -0.46, -0.10, -0.01, -0.33, -0.39, -0.44, -0.25, -0.26, -0.12, -0.31, -0.14, -0.38, -0.08, -0.25, -0.20, -0.16, -0.93], 
    [0.31, -0.78, -0.35, 1.62, 0.89, -1.19, -1.81, -4.21, -1.77, 0.10, 0.38, -2.32, 0.58, 0.42, 1.73, 0.28, 0.46, 1.07], 
    [-0.48, -0.40, 0.04, -0.25, -0.49, -0.17, -0.12, -0.20, -0.44, -0.16, -0.13, 0.01, -0.38, 0.02, -0.13, 0.05, -0.25, -1.06], 
    [-0.51, -0.33, -0.09, -0.09, -0.44, -0.22, -0.19, -0.18, -0.47, -0.28, -0.22, 0.01, -0.45, -0.14, -0.15, -0.04, -0.13, -0.51], 
    [1.90, 1.74, 1.48, 2.94, -0.55, 0.46, 0.89, -2.82, -3.12, 0.92, 0.54, -2.47, 1.79, -1.82, 2.90, -5.75, 0.92, 2.70], 
    [2.16, 3.22, -2.63, 0.98, 0.54, 0.75, -1.56, 1.22, 0.31, 1.42, 1.02, -2.04, 0.41, -1.65, -4.19, 2.17, 0.79, 1.13], 
    [1.93, -2.77, -0.38, 1.41, 1.08, 0.71, 1.18, -2.47, 0.56, 1.12, 0.29, -2.17, 0.22, -1.00, -2.29, -2.56, 0.39, -0.51], 
    [-0.59, -0.32, -0.17, 0.15, -0.98, -0.12, -0.31, -0.28, -0.81, -0.24, -0.14, -0.20, -0.31, -0.36, -0.23, 0.04, 0.01, -0.57], 
    [1.42, 2.02, 0.16, 4.06, 1.96, -2.34, 0.20, 1.05, -3.47, 1.46, -1.34, -2.21, -3.79, 0.53, 0.95, 0.82, -2.30, 1.45], 
    [-0.91, 1.47, -1.28, 0.06, 1.54, -1.73, 1.14, 2.10, 0.84, 0.91, 0.10, -0.96, 1.20, -0.69, -3.59, -2.85, -0.47, -1.83], 
    [-0.04, 2.63, 0.73, -3.60, -2.49, 0.44, 0.20, 1.21, 1.34, 0.08, 0.36, 0.58, 5.72, -0.81, -4.35, -2.21, 0.32, -3.06], 
    [0.73, 1.20, 0.78, -1.99, -0.34, 1.76, -0.74, 1.29, -1.13, -1.34, -0.78, 0.76, -1.47, 0.15, 0.64, 1.63, -1.69, 0.63], 
    [-0.63, -0.59, -0.06, -0.26, -0.21, -0.10, -0.27, -0.04, -0.01, -0.44, -0.22, 0.13, -0.63, 0.03, -0.35, 0.04, -0.34, -0.98], 
    [-0.21, -0.17, -2.87, 0.60, 0.50, -0.40, -0.97, -0.42, 0.29, -0.11, 0.05, -1.06, 0.00, 0.43, 0.51, 0.30, -0.26, 0.78], 
    [1.71, 0.61, 0.05, -3.02, 3.62, 0.44, 0.75, 0.17, -1.15, -0.90, -2.37, -0.45, -4.29, 0.83, 0.61, 1.66, -2.08, 1.32], 
    [-3.18, -0.67, -0.97, -0.49, 1.08, -0.01, 0.96, 0.41, 1.71, -1.27, 0.36, 0.09, 0.02, -1.35, -1.51, -2.25, 1.01, -0.81], 
    [-1.77, 1.33, 0.92, -0.63, -0.76, 1.40, -0.95, 0.47, -1.18, -0.84, -1.33, 0.74, -2.92, 0.26, 0.50, 1.09, -0.58, 0.54], 
    [-1.20, 3.51, -2.34, 0.38, 0.42, -2.04, -0.12, 1.18, 0.66, 0.52, 0.36, 0.88, 0.58, -1.64, -3.69, 2.40, -1.07, -0.59], 
    [-0.51, -0.31, -0.04, 0.02, -0.23, -0.30, -0.21, 0.01, -0.35, -0.27, -0.37, -0.10, -0.45, -0.14, -0.08, -0.08, -0.39, -1.30], 
    [1.12, -3.45, -2.43, 0.73, 1.16, 1.47, -0.20, 0.77, 0.57, -1.54, -2.02, -0.11, 3.50, 0.96, 1.69, 0.02, -2.06, 0.74], 
    [-0.15, -0.20, 0.43, 0.10, -0.17, -0.19, -1.90, 0.07, -0.26, 0.09, -0.12, 0.26, -0.14, -0.29, 0.19, 0.42, 0.19, -2.00], 
    [-0.60, -0.45, 0.09, 0.06, -0.22, 0.13, -0.40, -0.51, -0.63, 0.18, -0.85, -0.72, -0.66, 0.30, -0.17, 0.01, 0.09, -0.42], 
    [-0.60, -1.41, 1.05, -2.17, -0.66, 1.49, 1.41, -0.99, -0.21, 1.26, -1.76, -0.75, -0.52, 1.19, -0.12, -2.32, 2.09, -1.24], 
    [-3.43, 2.00, 1.19, -2.08, -1.90, -2.27, 0.68, -1.22, -1.50, 0.89, 1.60, 0.46, -2.35, -0.31, 0.46, 0.73, -1.72, 0.90], 
    [0.34, -1.20, 0.82, -4.32, -1.47, 0.47, 0.41, 0.20, 1.36, 0.30, 0.41, 0.88, 1.33, 0.68, -1.20, -2.44, -0.19, -0.50], 
    [0.53, 1.55, -1.27, 0.64, 0.33, 0.17, 0.33, 0.22, 0.18, -3.42, 0.24, 0.56, -0.07, -2.98, 1.59, 0.68, 0.50, 0.63], 
    [1.03, 2.18, 1.10, -2.94, -1.10, -1.74, 0.25, 0.86, -0.25, 0.63, 0.50, -0.16, 1.35, 0.80, -4.22, -0.56, 0.13, -1.07], 
    [-0.51, -0.48, 0.04, -0.14, -0.27, -0.34, -0.28, -0.03, -0.42, -0.30, -0.28, -0.06, -0.54, -0.04, -0.12, -0.02, -0.21, -1.12] ]
    
    #Connection weights from input units (rows) to hidden units (columns):
    bias_in_hid =  [2.83, 2.56, 2.70, 1.96, -2.40, -3.66, 1.64, 4.58, -6.68, 5.06, 1.63, -1.78, 0.87, 2.10, -3.22, 6.06, 3.16, 0.57, 4.77, 1.61, 3.68, 2.89, 6.74, 2.71, 2.51, 1.73, 2.80, 1.00, 1.74, 0.17, 7.10, 3.50, 1.13, 4.95, 6.68, -5.36, 0.45, 1.91, 5.78, 3.43, 6.37, 1.44, 9.52, 1.54, 10.21, 0.40, 2.16, 0.87, -1.61, -0.22, 3.28, -0.36, 1.47]
    in_hid = [ [0.67, -12.48, 1.29, -3.79, -5.39, 2.33, 1.14, 2.48, 8.35, 8.74, 1.30, 0.27, -1.01, -0.36, 5.27, -4.09, -0.26, 0.53, -0.38, 2.88, 2.38, 0.70, -2.70, 1.94, 3.22, 0.91, 6.19, 0.53, 1.71, 10.68, -6.38, 1.65, 2.45, 11.52, -2.57, -6.11, 3.29, 0.23, 0.03, 3.50, 0.12, 3.03, -3.60, 0.22, -3.03, -2.12, 1.81, 0.60, 6.53, -1.73, 0.25, -0.31, 0.58], 
    [0.17, -1.88, 0.06, -1.45, 1.15, -0.31, 0.12, 0.12, 2.39, -0.28, 0.28, -1.17, 0.16, 1.10, -0.33, 0.28, 1.31, 0.27, -0.09, -0.40, 3.01, 0.29, -0.67, 0.16, -0.09, 0.40, 0.47, 0.14, 0.19, -1.55, -0.87, -1.27, 0.14, 0.92, -1.19, -0.72, 0.39, 0.31, -0.37, 0.16, -1.41, 2.03, -1.01, 0.10, -2.24, 1.31, 0.59, -0.18, 1.51, -0.96, -1.22, -0.68, 0.12], 
    [-0.14, 0.00, -0.08, -2.37, 4.29, -2.72, 0.18, 0.65, 2.93, 2.98, 0.54, -1.04, -0.13, 2.74, -6.18, 1.30, 1.95, 0.25, -3.44, 0.63, 4.60, 0.61, 2.01, 0.38, 6.18, 0.35, -1.81, 0.32, 0.32, -8.47, -8.04, -5.59, -0.13, -0.01, -3.52, 0.67, 1.86, 0.86, -0.65, 2.36, 3.29, 5.46, -4.54, 0.37, 0.66, 1.23, 0.69, 2.67, 2.60, 4.15, -0.97, -2.05, 0.57], 
    [0.79, -16.63, 0.56, 0.50, -1.16, -0.17, 0.48, 0.28, 5.60, -7.32, 0.49, -0.41, 1.08, -0.64, 3.04, 5.28, 2.52, 0.83, -5.58, 2.49, 3.72, 1.21, -7.39, 0.51, 0.39, 1.06, 5.18, 0.65, 0.60, 6.10, -6.85, 0.52, 0.93, 5.73, -6.49, -16.49, -0.72, 0.52, -0.11, -3.06, -1.01, 4.35, -11.05, 0.92, 2.72, 2.79, 1.31, 0.17, -4.26, -10.39, 2.17, -13.54, 0.84], 
    [2.62, 3.00, 2.09, 4.58, -6.35, -4.59, 1.50, 2.12, -12.78, -9.04, 1.39, -5.00, 4.51, 1.92, -0.74, 2.09, 2.87, 2.81, -1.07, -1.04, -2.64, 2.61, -1.10, 0.74, -7.90, 2.18, -1.00, 2.58, 1.32, -9.44, 8.01, -0.97, 0.72, 1.09, 2.02, -3.12, -2.47, 2.18, 2.82, 0.51, -0.10, 0.42, 4.07, 3.55, 1.96, 4.67, 1.48, 2.18, -3.83, -3.80, 0.48, -0.71, 2.64], 
    [0.09, -2.21, -0.01, 1.00, -1.90, 2.60, 0.22, -1.55, 5.60, -0.40, 0.27, 1.06, 0.53, 0.32, 0.09, -1.29, 0.90, 0.41, -1.61, 0.13, 1.94, 0.29, -3.08, 0.39, 3.29, 0.20, 0.30, 0.18, 0.27, 5.49, -1.83, 1.65, 0.47, -4.97, -1.62, 0.22, -1.04, 0.08, 0.05, -4.85, 2.43, -0.17, -5.09, 0.19, -2.15, 1.48, -0.06, 0.00, -1.28, 0.03, -0.28, -3.80, 0.21], 
    [0.47, -1.29, 0.45, -3.56, -2.58, 1.03, 0.46, -0.24, 1.50, 8.99, 0.36, -2.94, -0.61, 0.73, 2.52, 2.14, 2.80, -0.14, 9.00, 0.94, 4.95, 0.69, 3.39, 1.30, 4.00, 0.66, 6.23, -0.22, 0.38, 8.68, 8.22, 6.57, 1.02, -6.37, -2.15, -0.59, -2.75, -0.09, 3.03, -7.15, 0.59, -0.26, 1.52, -0.43, -0.85, 1.85, 0.48, -2.10, -0.92, -0.80, -2.06, -0.15, -0.15], 
    [0.29, -0.77, 0.23, 1.76, 2.26, -1.47, 0.12, -1.21, 7.00, -2.28, 0.15, -0.46, 1.12, 0.22, -7.09, 1.91, 0.03, 0.18, -0.39, -4.55, 1.58, 0.43, -3.50, 0.32, 6.72, 0.45, -2.39, 0.50, 0.25, -0.58, 3.33, 4.02, 0.24, -7.46, -0.07, 1.34, -0.54, 0.99, -0.52, -2.08, 5.97, 2.36, -2.11, 0.41, -1.94, 0.38, 0.87, 3.32, 0.51, 1.48, 0.93, -7.56, 0.30], 
    [-0.08, 10.76, 0.58, 0.26, 10.18, 6.69, 1.20, 0.82, 7.78, 10.08, 1.36, 17.33, 1.29, -0.11, 0.05, -5.22, -2.08, 0.81, 0.96, -0.40, 7.52, -0.02, 6.99, 1.22, 4.95, 0.67, -4.49, 1.09, 0.88, 2.31, -11.23, 0.27, 0.50, -6.33, -2.95, 11.63, 1.62, 1.56, -0.46, 2.01, -2.51, -4.56, -6.57, 0.89, 7.37, -2.14, -0.13, -1.12, 1.63, 10.80, -0.44, 5.15, 0.81], 
    [-0.19, 0.80, -0.15, -1.82, -0.11, 0.81, 0.47, 0.54, -1.09, -1.28, 0.37, -1.70, 0.76, 0.70, -3.19, 0.07, -0.44, 0.35, -1.83, 0.81, -0.27, -0.12, 1.85, -0.20, -4.42, 0.35, 1.71, 0.52, 0.14, -2.12, -0.23, -2.58, 0.17, 2.43, 2.24, 1.04, -1.79, 0.31, -0.21, 2.15, 2.30, 0.21, 1.13, 0.31, -3.33, 0.14, 0.31, 0.75, 1.72, 0.37, -2.79, 4.13, 0.47], 
    [-0.03, 7.51, -0.04, -4.11, 5.25, 7.13, 0.43, 0.23, -0.99, 0.72, 0.49, 9.52, 1.43, -1.61, 4.04, 1.39, -2.35, 0.71, 0.40, -1.49, -3.44, -0.64, 4.04, -0.43, -7.84, 0.63, 3.23, 0.64, 0.24, 5.40, -4.20, 4.72, 0.32, -4.51, 1.19, 7.01, -5.22, -0.03, -1.57, -1.78, -1.95, -5.44, -5.12, 0.37, -1.48, -1.10, 0.67, 3.63, 0.09, 5.78, -4.51, 7.54, 0.37], 
    [0.84, -4.96, 0.74, -3.00, 0.69, -0.83, 0.81, -0.47, 3.32, 2.82, 0.67, -5.00, 0.47, 0.31, 4.07, -1.54, -0.76, 1.00, -1.67, 0.46, -6.70, 0.39, -1.16, -0.02, 5.12, 0.63, -1.93, 0.77, 0.55, 7.19, 1.66, 0.59, 1.08, 5.75, 5.20, 3.27, -0.77, 0.21, -3.07, 0.31, 2.99, 0.17, -1.88, 0.76, -7.78, -0.23, 0.52, -0.04, 1.63, -1.13, 0.19, 4.12, 0.65], 
    [0.18, -1.88, 0.13, 1.57, -2.58, 6.81, 0.59, -0.52, 11.22, -3.59, 0.84, 2.82, 1.05, 1.02, 1.13, -3.20, 0.69, 0.78, -4.90, 0.79, 2.95, 0.25, -0.92, 0.24, -3.03, 0.68, 1.49, 0.78, 0.47, 5.66, -9.95, -2.77, 0.72, -2.03, -1.14, 2.38, -2.07, 0.47, 0.15, -3.58, -1.26, 0.04, -0.75, 0.51, -0.69, 1.51, 0.10, -2.17, 2.68, 1.56, -1.19, -1.05, 0.55], 
    [1.06, 0.29, 1.18, 1.26, 6.02, -5.26, 1.26, 1.95, 2.78, 6.61, 0.97, -7.06, 0.28, -0.15, -3.98, 3.54, -0.79, 0.31, -1.06, -0.57, 1.24, 0.94, 1.84, 1.43, 9.78, 0.96, 0.64, 0.44, 1.03, 1.99, 3.75, 4.20, 0.64, 1.36, 4.21, -2.62, -4.31, 1.20, 2.05, -0.20, 7.72, -0.11, 1.67, 0.31, -1.68, -1.70, 0.89, 0.56, -2.08, -3.15, 2.60, -3.61, 0.69], 
    [0.54, -3.77, 0.37, -1.65, 10.11, -0.26, 0.76, 0.46, -1.39, -15.14, 0.71, 4.74, 0.98, 0.82, -2.62, 4.59, 0.20, 1.38, 0.72, -1.86, -1.86, 0.74, -2.62, 0.07, -10.72, 0.50, 2.68, 1.38, 0.90, -4.76, -4.39, -4.54, 1.01, 6.54, -8.16, -4.89, 9.16, 0.95, -3.86, 10.51, -5.62, 4.62, -6.16, 1.20, 0.64, 0.94, 1.65, 0.99, 4.24, 0.18, 0.08, -3.73, 1.46], 
    [0.06, -0.85, 0.08, -2.99, 1.16, 0.73, 0.55, 0.18, 1.01, -0.99, 0.28, 2.58, -0.08, 0.68, 0.21, 0.02, 0.52, 0.32, -2.06, 0.86, -2.65, 0.22, -0.11, 0.07, -1.34, 0.18, -1.10, 0.27, 0.35, -0.29, -3.12, -2.52, 0.25, 2.07, -0.56, 2.10, 2.96, 0.30, -3.28, 2.49, -0.08, 2.06, -2.12, 0.37, -2.07, 0.24, 0.51, 0.63, 1.28, 1.64, -0.59, 2.93, 0.37], 
    [0.17, -0.34, 0.10, 0.64, -3.01, -6.68, 0.13, 0.15, -10.26, -1.68, -0.01, -10.28, 0.17, 0.61, 0.02, -0.93, 0.49, 0.11, 4.77, 0.77, -2.63, 0.26, -0.11, 0.10, -3.95, 0.03, -1.47, 0.14, 0.05, -13.18, 14.32, -1.75, 0.20, 1.05, 0.32, 1.66, 1.24, 0.16, 0.13, 0.76, 0.02, 1.30, 13.87, 0.08, -6.08, 0.34, -0.19, -1.45, 1.05, -1.08, 0.73, 6.62, 0.04], 
    [0.50, 5.46, 0.25, 3.35, -3.46, 3.01, 1.03, -2.06, -4.89, 1.16, 0.99, 0.44, 2.17, 1.99, 2.24, -4.32, 3.14, 1.83, 2.61, 2.89, -0.88, 1.22, -1.74, 1.20, -1.63, 1.06, 2.22, 1.30, 0.88, -1.42, 6.58, -0.25, 1.36, -13.49, -3.98, 8.24, -0.52, 0.89, 0.47, -8.76, 1.01, -1.32, -0.20, 1.12, -7.24, 4.99, -0.30, -3.43, -3.10, 2.86, 0.62, 4.93, 1.15], 
    [0.57, -2.55, 0.75, 0.05, 0.64, 7.65, 0.67, -0.15, 1.93, 0.13, 1.06, 4.13, 1.62, -0.50, 8.92, -2.69, -0.73, 1.44, -1.19, 0.75, -1.93, 0.43, -3.57, 0.43, -0.93, 0.74, -3.51, 1.18, 0.90, -1.72, -5.07, -1.26, 1.33, 1.61, -4.06, 5.45, 0.92, 0.70, -1.80, -3.36, -3.74, -0.27, -2.87, 1.15, -1.99, 0.22, 0.69, 1.64, -0.11, 3.60, -1.02, 2.71, 0.88], 
    [0.54, 15.05, 0.56, 0.82, 2.26, 5.92, 0.81, -1.77, 6.06, -5.73, 0.76, -3.42, 1.92, -0.53, -3.59, 0.80, -2.14, 1.19, -4.94, -4.52, -14.44, -0.15, -2.92, 0.12, -1.90, 0.86, -7.83, 1.05, 0.76, 8.73, -0.31, 1.60, 1.03, -15.99, 4.27, 19.15, -2.56, 0.84, -1.81, -3.63, 7.29, -1.48, 1.20, 1.07, -0.82, -1.00, 1.02, 5.66, -1.97, 8.65, -1.52, 3.75, 0.86], 
    [0.60, 1.62, 0.39, 4.49, 1.15, -3.00, 0.68, -0.13, -5.52, -5.29, 0.87, -3.09, 0.90, 1.68, 0.46, -4.38, -0.13, 0.74, 2.02, 2.62, 2.39, 0.55, 2.06, 0.67, -1.29, 0.01, -6.98, 0.50, 0.52, -16.97, 5.38, -4.96, 0.38, 0.02, 0.95, 7.62, 3.07, 1.04, -0.98, -0.40, 2.16, -0.05, 14.32, 0.41, -2.58, -0.07, -1.03, -5.13, 2.62, 4.62, 3.45, 7.44, 0.61], 
    [0.57, -7.19, 0.09, -0.24, -3.78, 3.01, 0.49, -0.72, 4.37, -6.07, 0.38, 3.73, 0.94, -0.17, 4.07, -3.00, -0.22, 0.81, -4.86, 1.24, -3.45, 0.22, -2.73, -0.41, -4.77, 0.35, 0.85, 0.46, 0.26, 6.10, -3.23, -0.21, 0.34, 5.16, 3.10, -2.54, -0.86, 0.06, -3.65, -0.14, -0.30, -0.44, -0.78, 0.70, -5.18, 0.66, -0.05, -1.46, 0.82, -2.37, 0.19, 1.32, 0.55], 
    [-0.51, 4.84, -0.02, 0.00, 5.48, 1.24, 0.19, 0.64, -2.20, 4.12, -0.07, 7.77, 0.61, 0.02, -3.58, 1.51, 0.70, -0.05, 0.67, -2.47, 3.83, 0.04, 0.75, 0.28, -0.39, 0.22, -0.67, 0.16, 0.08, -3.28, -0.14, 0.37, -0.16, -1.60, -3.19, 1.04, 3.05, 0.45, 1.81, 4.27, -2.66, 0.24, -6.65, 0.11, 1.78, 0.45, 0.72, 3.76, -1.59, 2.49, -1.78, 0.02, 0.18], 
    [0.05, -0.55, -0.07, 0.34, -1.47, 0.77, 0.00, 0.02, 1.58, -0.09, 0.07, 0.03, -0.01, 0.01, 0.28, -1.02, 0.19, -0.01, -1.60, 0.20, -0.32, 0.05, -0.77, 0.06, 0.48, -0.08, -0.75, -0.05, 0.08, 1.00, -1.12, -0.76, 0.01, 0.62, 0.06, 0.29, 0.44, 0.03, -0.16, 0.13, -0.13, 0.44, -0.01, 0.01, -0.42, 0.06, -0.05, 0.08, 0.15, -0.01, 0.16, -0.13, 0.13], 
    [-0.14, 0.57, 0.01, -2.34, 5.83, -4.12, 0.16, 0.48, -6.34, 4.63, 0.17, -5.05, -0.13, -0.14, -0.23, 3.05, -0.17, -0.03, 9.58, -1.95, -0.05, -0.40, 2.97, 0.26, -1.88, 0.08, 0.19, 0.16, 0.20, -4.85, 14.07, 0.80, 0.30, 1.68, 0.18, 2.71, 2.50, 0.07, 1.93, 2.85, -2.43, 0.20, 6.45, -0.08, -3.19, -0.56, 0.91, -0.01, 1.38, -0.64, -1.85, 6.19, 0.03], 
    [-0.61, 5.80, -0.40, -7.09, 3.61, -0.93, 0.28, 1.34, -3.64, 3.62, 0.46, 0.42, 0.90, 2.67, -6.24, 2.52, 1.20, 0.34, 1.40, -2.15, 2.93, -0.40, 6.02, -0.21, -3.94, 0.64, 2.05, 0.48, 0.07, -8.15, -4.42, -1.73, -0.28, 3.90, 0.96, -0.19, -2.38, 0.56, 0.80, 3.98, 0.10, 1.17, -4.01, 0.31, -1.08, 1.50, 1.13, 5.76, 2.98, 4.91, -8.75, 3.55, 0.45], 
    [0.13, 0.19, -0.05, 0.17, -1.43, 0.52, 0.11, -0.10, -0.29, 0.21, -0.05, -0.45, -0.01, 0.12, 0.12, -0.51, 0.17, 0.08, -1.12, 0.17, -2.18, 0.01, -0.65, 0.01, 0.08, 0.07, -0.99, 0.06, 0.02, 0.36, 0.34, -0.57, -0.05, 0.64, 1.47, 1.05, 0.41, -0.07, -0.12, 0.19, 0.53, 0.14, 0.64, -0.05, -0.66, 0.03, 0.11, 0.23, -0.44, 0.25, 0.00, 1.11, 0.00], 
    [0.29, -1.64, -0.18, -1.64, 3.81, -2.23, 0.10, -0.31, 1.17, 0.65, 0.35, -3.80, -0.09, 1.72, 0.78, 0.10, 0.92, 0.22, 5.91, -1.12, 3.44, -0.03, 3.37, -0.19, 0.01, 0.05, 1.74, 0.09, -0.07, 0.12, 5.92, 0.36, 0.08, 2.78, 2.71, 0.30, 0.39, 0.09, 0.09, 1.19, -1.69, -0.03, 5.58, -0.02, -4.31, 1.09, -0.02, -3.47, 3.73, -0.92, -1.33, 2.14, 0.02], 
    [-0.02, 0.03, 0.01, -0.04, 0.17, -0.04, -0.01, 0.05, -0.10, -0.06, 0.06, -0.04, 0.02, 0.06, -0.03, 0.28, 0.08, -0.08, 0.01, 0.02, -0.13, 0.02, 0.05, 0.04, -0.03, 0.08, -0.12, -0.11, -0.07, 0.03, -0.05, 0.00, -0.03, 0.11, 0.03, -0.12, 0.17, 0.05, -0.09, 0.06, 0.03, 0.09, 0.02, 0.04, 0.14, 0.00, -0.07, -0.07, -0.12, -0.08, 0.12, -0.02, 0.05], 
    [0.08, -0.27, 0.01, 0.47, -0.21, 1.75, -0.10, 0.05, 2.13, -0.41, -0.06, 2.23, 0.13, 0.03, 0.10, -0.26, 0.07, 0.00, -1.58, 0.13, 0.11, -0.02, -0.12, -0.11, 0.12, 0.13, 0.37, -0.03, -0.01, 2.03, -2.89, -0.13, 0.00, 0.08, -0.11, -0.42, 0.10, -0.08, 0.02, 0.06, -0.13, -0.01, -1.47, 0.06, 0.98, 0.05, 0.08, 0.30, 0.07, 0.69, 0.09, -1.22, 0.12], 
    [-0.35, -1.11, 0.14, 2.64, 4.64, 0.46, 0.04, 1.02, 1.32, 2.72, 0.10, -0.86, 0.34, -3.25, 0.56, 1.19, -4.71, 0.10, -6.07, -0.23, -2.27, -0.74, -0.49, -0.28, 3.80, -0.08, -1.81, -0.03, 0.07, 0.15, -1.76, 2.04, 0.03, 1.59, 0.79, 0.83, -4.64, -0.08, 1.56, 1.11, 3.61, -2.69, 0.58, 0.04, 1.09, -4.17, 0.05, 4.73, -1.89, 0.54, 1.97, 0.04, 0.12], 
    [0.09, -2.24, 0.11, 0.51, -2.98, -0.21, 0.02, -0.13, -0.15, -2.41, 0.13, -1.18, 0.12, 0.14, 0.67, -0.75, 0.31, -0.03, 1.84, 0.90, 2.50, 0.12, -0.56, 0.20, -1.80, -0.04, 0.92, -0.03, 0.09, 0.29, 0.06, 0.27, 0.10, 0.97, -0.40, -2.61, -0.83, -0.11, 0.37, -2.32, -0.19, -0.28, 1.09, 0.13, 1.27, 0.40, -0.29, -2.62, 0.31, -2.41, 0.03, -1.85, 0.05], 
    [0.04, -0.17, 0.08, 0.47, -0.78, 1.51, 0.00, 0.02, 1.59, -0.01, 0.07, 1.55, 0.02, 0.11, 0.06, -0.47, 0.12, 0.01, -1.46, 0.17, -0.37, 0.10, -0.24, -0.01, 0.06, 0.09, 0.09, 0.06, 0.08, 1.72, -1.86, -0.16, -0.02, 0.06, 0.21, 0.18, 0.01, -0.07, 0.01, 0.07, 0.07, 0.01, -0.92, 0.00, 0.33, 0.14, -0.03, 0.27, 0.16, 0.59, 0.20, -0.38, 0.10], 
    [-0.01, -0.01, 0.12, 0.21, -0.64, 0.19, 0.06, 0.03, -0.33, -0.07, 0.03, -0.41, -0.04, 0.07, 0.07, -0.24, -0.05, -0.05, -0.53, 0.14, -1.14, 0.06, -0.37, 0.03, -0.05, 0.09, -0.53, 0.09, -0.08, 0.06, 0.34, -0.33, -0.04, 0.37, 0.90, 0.36, 0.17, 0.04, -0.15, 0.07, 0.27, 0.06, 0.33, 0.07, -0.29, 0.11, -0.04, 0.26, -0.29, 0.11, 0.00, 0.47, 0.01], 
    [0.31, 1.20, -0.02, -2.42, 1.23, -0.19, -0.07, -0.33, -2.57, -2.71, 0.19, -3.48, 0.10, 1.39, 0.74, 1.50, 0.64, 0.34, 1.13, -1.38, -5.08, -0.15, 0.60, -0.42, -1.92, 0.08, -1.89, 0.04, -0.06, -1.85, 1.92, -0.39, 0.04, 4.36, 3.93, 0.95, 0.40, -0.06, -0.87, 1.85, -0.11, 0.11, 1.57, 0.27, -1.91, 0.90, 0.17, 1.90, -0.07, 1.46, -3.44, 2.02, 0.19], 
    [0.03, 0.02, -0.04, 0.15, 0.51, 0.49, -0.06, -0.02, -0.36, -0.30, 0.08, 0.67, -0.03, 0.06, 0.22, 0.25, 0.03, 0.08, -0.34, 0.08, -0.43, 0.12, -0.06, -0.06, -0.14, 0.02, -0.38, 0.01, 0.01, -0.03, -0.49, -0.13, 0.08, 0.20, 0.28, 0.08, 0.38, 0.07, -0.07, 0.14, -0.04, -0.12, -0.25, 0.04, 0.44, -0.04, 0.01, 0.23, -0.50, 0.21, 0.11, 0.06, -0.02], 
    [0.09, 0.15, 0.09, 0.06, 0.24, 0.13, 0.10, 0.00, -0.07, 0.00, -0.05, 0.28, -0.01, -0.09, 0.05, -0.02, -0.08, 0.08, -0.03, 0.03, 0.13, 0.02, 0.00, -0.05, -0.08, 0.09, -0.01, -0.03, 0.05, 0.13, 0.00, -0.07, -0.06, -0.01, -0.09, 0.00, 0.00, -0.06, 0.08, 0.17, -0.26, -0.02, -0.08, 0.05, -0.03, 0.05, 0.07, -0.05, -0.14, 0.00, -0.01, 0.10, -0.01], 
    [0.18, -3.02, -0.04, -0.05, 0.49, -2.99, 0.17, -0.49, -0.11, -0.75, 0.05, -2.61, -0.14, 0.94, 0.40, -1.52, 0.60, 0.11, 2.74, 0.57, 0.37, 0.26, 1.36, -0.07, -0.21, -0.02, 1.07, 0.07, -0.02, -1.70, 5.50, -1.23, 0.15, 0.59, 2.31, 1.36, 1.06, 0.09, -1.39, 0.02, 0.16, 0.41, 4.22, -0.07, -5.40, 0.69, -0.25, -4.29, 3.00, -1.54, 1.18, 3.26, 0.11], 
    [0.04, -0.01, -0.03, 0.01, 0.03, 0.03, -0.09, 0.10, -0.05, -0.14, 0.00, -0.12, -0.04, -0.03, 0.01, 0.12, 0.08, 0.06, -0.05, 0.01, -0.04, -0.07, 0.09, 0.07, -0.02, -0.04, -0.10, 0.04, 0.04, -0.13, -0.12, 0.02, 0.10, 0.03, 0.13, 0.00, 0.07, -0.04, 0.06, 0.02, 0.13, 0.05, 0.11, 0.00, 0.18, 0.09, 0.00, -0.08, -0.10, -0.04, 0.04, 0.00, -0.07], 
    [0.08, -0.02, -0.04, 0.02, -0.13, -0.02, 0.04, -0.01, 0.07, 0.08, -0.09, -0.06, -0.01, -0.08, 0.07, -0.17, 0.00, -0.09, -0.15, 0.06, -0.11, -0.04, -0.06, -0.04, -0.09, -0.05, -0.12, 0.03, 0.05, -0.07, -0.07, 0.00, -0.04, -0.04, 0.00, 0.13, 0.09, -0.06, -0.10, 0.11, 0.04, 0.01, 0.02, -0.03, -0.11, 0.05, -0.06, 0.07, 0.04, 0.00, -0.05, 0.02, 0.02], 
    [0.05, -0.11, -0.01, -0.07, 0.37, -1.60, 0.07, 0.08, -2.64, -1.16, -0.08, -1.68, 0.01, 0.15, -0.23, 0.53, -0.04, -0.04, 1.39, -0.03, -0.06, 0.06, 0.06, 0.09, -1.38, 0.06, 0.07, 0.00, -0.04, -3.16, 2.12, 0.05, 0.00, 0.03, -0.36, -0.22, 0.15, 0.10, 0.08, 0.03, -0.12, 0.03, 1.67, -0.03, -0.37, 0.04, -0.03, -0.22, -0.01, -0.40, 0.09, 0.49, 0.01], 
    [0.08, -0.15, -0.01, 0.04, -1.27, 0.33, 0.03, 0.00, 0.58, 0.71, -0.10, 0.00, -0.06, 0.08, 0.14, -0.71, -0.01, -0.04, -0.49, 0.11, -0.44, 0.07, -0.32, -0.08, 0.15, 0.10, -0.04, 0.02, 0.08, 0.48, 0.14, -0.13, 0.06, 0.04, 0.22, 0.49, -0.05, 0.03, -0.07, 0.05, -0.02, 0.22, 0.24, 0.01, -0.84, 0.01, -0.07, 0.18, 0.30, 0.03, -0.13, 0.74, -0.10], 
    [-0.12, 0.78, -0.01, -1.72, 0.56, -1.94, 0.10, 0.29, -2.87, 3.43, 0.16, -2.10, -0.10, 0.64, -0.30, -0.12, 0.47, 0.00, 4.77, 0.02, 2.36, -0.09, 2.54, 0.25, 0.31, 0.09, 1.20, 0.01, -0.05, -3.30, 4.13, 0.03, 0.08, 0.86, -0.51, 0.16, 0.14, 0.09, 1.01, 0.56, -0.66, 0.05, 1.82, -0.15, -1.30, 0.39, 0.07, -0.50, 1.50, 0.51, -1.72, 2.11, 0.03], 
    [0.06, 0.10, -0.01, 0.06, 0.02, 0.40, -0.10, 0.09, 0.24, -0.12, -0.07, 0.49, 0.00, 0.09, 0.09, 0.00, -0.07, 0.05, -0.22, 0.11, -0.07, 0.07, -0.07, 0.09, 0.02, -0.05, -0.16, -0.07, -0.03, 0.16, -0.57, 0.03, -0.02, 0.11, -0.04, 0.05, 0.17, -0.06, -0.03, 0.09, -0.08, -0.04, -0.18, -0.02, 0.28, -0.06, 0.04, 0.14, -0.13, 0.20, 0.01, -0.22, 0.03], 
    [0.05, -0.05, 0.10, 0.13, -0.02, 0.09, 0.01, 0.06, 0.20, -0.10, -0.05, 0.26, 0.09, 0.04, 0.01, -0.08, -0.08, -0.04, -0.24, 0.08, 0.05, 0.05, -0.02, 0.08, -0.02, -0.04, 0.12, -0.06, -0.05, 0.10, -0.34, 0.04, 0.04, 0.05, -0.03, -0.12, -0.07, 0.09, -0.07, 0.02, -0.05, 0.04, -0.08, 0.03, 0.08, 0.08, -0.09, 0.01, -0.04, 0.06, -0.04, -0.06, 0.01], 
    [-0.25, -0.65, -0.22, -0.42, 3.28, 0.11, 0.06, -0.32, 1.12, 1.56, 0.15, -1.50, 0.19, -0.28, 0.63, 0.93, -0.36, 0.24, -2.36, -0.29, -0.65, -0.08, -0.71, -0.03, 2.16, 0.20, 0.51, -0.06, 0.13, 0.02, 0.78, 0.80, 0.21, -1.17, -0.91, 0.48, -1.77, -0.01, 0.21, -0.22, 0.81, -0.26, -1.06, -0.17, -3.68, 0.18, 0.13, 2.62, -1.24, 0.68, -0.86, 0.16, 0.01], 
    [0.04, 0.01, 0.00, 0.06, 0.01, -0.09, -0.05, 0.02, -0.04, 0.01, 0.01, -0.01, -0.03, 0.09, 0.02, 0.11, -0.04, -0.09, 0.03, 0.05, -0.11, 0.05, 0.00, 0.00, -0.05, 0.08, -0.15, -0.04, -0.01, 0.02, 0.02, -0.04, 0.09, 0.09, 0.18, 0.04, 0.04, -0.06, -0.03, 0.02, 0.05, 0.01, 0.08, 0.05, -0.02, -0.06, -0.01, 0.08, -0.11, 0.07, 0.05, -0.02, 0.00], 
    [0.04, -0.03, -0.15, -0.11, 0.30, 0.11, 0.14, -0.12, 0.45, 0.33, 0.02, 0.73, 0.08, 0.32, 0.10, -0.91, 0.16, 0.10, 1.39, -0.03, 1.90, -0.02, 0.77, 0.14, 0.25, -0.07, 0.76, 0.00, -0.08, 0.53, -0.28, 0.47, -0.02, 0.22, -0.16, -0.09, 0.11, 0.08, 0.17, -0.14, -0.31, -0.41, -0.65, 0.04, -0.46, 0.30, -0.14, -1.11, 0.83, 0.33, -0.45, -0.02, 0.02], 
    [0.06, 0.00, 0.01, 0.02, -0.06, -0.05, 0.03, -0.02, -0.01, -0.07, -0.04, -0.01, 0.02, 0.04, -0.02, 0.07, -0.09, 0.05, 0.02, 0.04, -0.05, 0.02, -0.10, -0.08, 0.02, 0.00, -0.16, 0.09, -0.10, -0.14, 0.09, -0.13, -0.04, 0.05, 0.01, 0.05, 0.07, -0.01, 0.00, -0.07, 0.17, 0.09, 0.10, 0.03, 0.17, 0.09, 0.06, -0.04, 0.00, 0.09, 0.03, 0.00, 0.06], 
    [0.04, 0.54, 0.11, -0.54, 0.42, 0.01, -0.06, -0.04, -0.03, 1.33, 0.05, -0.17, 0.03, 0.26, 0.05, 0.21, -0.03, -0.05, 0.58, -0.53, 0.53, -0.05, 0.70, -0.10, 1.01, 0.16, -0.34, -0.03, -0.01, -0.90, 0.19, 0.50, -0.06, -0.61, 0.35, 0.62, -0.84, -0.05, -0.01, -0.65, 0.06, -0.27, 0.33, 0.00, -0.09, 0.02, 0.14, 0.46, 0.11, 0.85, -0.70, 0.20, 0.06], 
    [0.14, -0.60, 0.04, -0.94, 0.08, 0.05, 0.18, -0.22, 0.70, -0.74, 0.12, 1.17, 0.07, 0.26, 0.28, -0.26, 0.11, -0.02, -0.57, 0.08, -0.89, 0.07, -0.08, -0.14, -0.31, 0.05, 0.08, 0.04, -0.07, 0.46, -0.71, 0.05, -0.02, 0.03, 0.41, 0.24, 0.37, 0.12, -1.37, 0.04, 0.21, 0.09, -0.62, -0.04, -1.40, 0.24, -0.01, -0.14, 0.51, 0.43, -0.22, 0.64, 0.06], 
    [0.00, 0.02, 0.09, 0.09, 0.08, 0.00, 0.06, -0.08, -0.03, 0.04, -0.06, 0.13, 0.07, 0.05, 0.08, -0.11, 0.04, -0.01, 0.03, -0.05, 0.15, 0.03, 0.07, -0.08, -0.10, -0.09, 0.05, -0.03, -0.08, 0.02, 0.01, 0.07, -0.06, 0.05, -0.05, 0.05, -0.05, 0.00, -0.05, 0.10, -0.02, -0.08, -0.03, 0.08, 0.01, 0.10, -0.08, -0.14, 0.00, 0.01, -0.08, 0.08, 0.03],
    [-0.03, -0.08, -0.10, -0.09, 0.02, -0.08, -0.04, -0.08, -0.03, -0.05, -0.05, 0.04, -0.05, -0.06, 0.02, -0.07, 0.04, -0.10, -0.01, 0.02, 0.00, -0.05, 0.01, 0.10, 0.03, -0.03, 0.02, 0.00, -0.08, -0.07, 0.08, 0.06, 0.09, -0.07, -0.08, 0.05, 0.10, -0.03, -0.06, -0.04, -0.04, -0.07, -0.05, -0.08, 0.05, 0.00, -0.01, 0.02, 0.04, 0.00, 0.07, -0.02, 0.04] ]           
    char_count = [0] * 53
    hid = [0] * 53
    out = [0] * 18
    for filestring in file:
        with open(filestring,encoding="utf8") as f:
            c = Counter()
            for x in f:
                c += Counter(x.strip())
                
            char_count[0] = c['a'] + c['A']
            char_count[1] = c['b'] + c['B']
            char_count[2] = c['c'] + c['C']
            char_count[3] = c['d'] + c['D']    
            char_count[4] = c['e'] + c['E']
            char_count[5] = c['f'] + c['F']
            char_count[6] = c['g'] + c['G']
            char_count[7] = c['h'] + c['H'] 
            char_count[8] = c['i'] + c['I']
            char_count[9] = c['j'] + c['J']
            char_count[10] = c['k'] + c['K']
            char_count[11] = c['l'] + c['L']    
            char_count[12] = c['m'] + c['M']
            char_count[13] = c['n'] + c['N']
            char_count[14] = c['o'] + c['O']
            char_count[15] = c['p'] + c['P']        
            char_count[16] = c['q'] + c['Q']
            char_count[17] = c['r'] + c['R']
            char_count[18] = c['s'] + c['S']
            char_count[19] = c['t'] + c['T']    
            char_count[20] = c['u'] + c['U']
            char_count[21] = c['v'] + c['V']
            char_count[22] = c['w'] + c['W']
            char_count[23] = c['x'] + c['X'] 
            char_count[24] = c['y'] + c['Y']
            char_count[25] = c['z'] + c['Z']
            char_count[26] = c['�'] + c['�']
            char_count[27] = c['�'] + c['�']    
            char_count[28] = c['�'] + c['�']
            char_count[29] = c['�'] + c['�']
            char_count[30] = c['�'] + c['�']
            char_count[31] = c['�'] + c['�'] 
            char_count[32] = c['�'] + c['�']
            char_count[33] = c['�'] + c['�']
            char_count[34] = c['�'] + c['�']
            char_count[35] = c['�'] + c['�']    
            char_count[36] = c['�'] + c['�']
            char_count[37] = c['�'] + c['�']
            char_count[38] = c['�'] + c['�']
            char_count[39] = c['�'] + c['�']   
            char_count[40] = c['�'] + c['�']
            char_count[41] = c['�'] + c['�']
            char_count[42] = c['�'] + c['�']    
            char_count[43] = c['�'] + c['�']
            char_count[44] = c['�'] + c['�']
            char_count[45] = c['�'] + c['�']
            char_count[46] = c['�'] + c['�'] 
            char_count[47] = c['�'] + c['�']
            char_count[48] = c['�'] + c['�']
            char_count[49] = c['�'] + c['�']
            char_count[50] = c['�'] + c['�']    
            char_count[51] = c['�'] + c['�']
            char_count[52] = c['�'] + c['�']
            
            max = 0
            for i in range(0, 53):
                if char_count[i] > max:
                    max = char_count[i]
            
            input_units = [0] * 53
            
            # Prints frequency of each letter
            print(filestring+ ":")
            for i in range(0, 53):
                input_units[i] = char_count[i]/max
                print(letters[i] +': %.5f,' % (char_count[i]/max), end=" ")
            print(" ")
                
def sigmoid(z):
    """The sigmoid function."""
    return 1.0/(1.0+np.exp(-z))

main()