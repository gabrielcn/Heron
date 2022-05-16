# Escreva um programa que peça ao usuário pelos lados de um triângulo ( 𝑎 ,  𝑏 ,  𝑐 ) e então compute a área de um triângulo utilizando a fórmula de Heron
import math
from math import sqrt

def area(a,b,c):
    p = (a+b+c)/2
    pa = (p - a)
    pb = (p - b)
    pc = (p - c)
    pf = p * pa * pb * pc
    raiz = math.sqrt(pf)
    return raiz

def main():
    a = float(input("Digite o valor do lado a: "))
    b = float(input("Digite o valor do lado b: "))
    c = float(input("Digite o valor do lado c: "))
    print("Área do triangulo = ", area(a,b,c))

main()
