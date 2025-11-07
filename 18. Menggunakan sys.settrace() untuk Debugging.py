import sys

def trace_calls(frame, event, arg):
    if event == 'call':
        print(f"Memanggil fungsi: {frame.f_code.co_name}")
    return trace_calls

sys.settrace(trace_calls)

def function_a():
    print("Function A is executing.")
    
function_a()


#Fungsi: Mengatur tracer untuk fungsi pemanggilan guna debugging.
#Kondisi: Ketika Anda memerlukan informasi tentang aliran pemanggilan fungsi dalam kode.

