print('Praktikum-2\n')
print('===============Ini and===============')
a = True
b = False
hasil = a and a
print('Nilai',a,'and',a,'adalah',hasil)
hasil = a and b
print('Nilai',a,'and',b,'adalah',hasil)
hasil = b and a
print('Nilai',b,'and',a,'adalah',hasil)
hasil = b and b
print('Nilai',b,'and',b,'adalah',hasil)

print('\n===============Ini or===============')
hasil = a or a
print('Nilai',a,'or',a,'adalah',hasil)
hasil = a or b
print('Nilai',a,'or',b,'adalah',hasil)
hasil = b or a
print('Nilai',b,'or',a,'adalah',hasil)
hasil = b or b
print('Nilai',b,'or',b,'adalah',hasil)

print('\n===============Ini not===============')
hasil = not a
print('Hasil not',a,'adalah',hasil)
hasil = not b
print('Hasil not',b,'adalah',hasil)

print('\n===============Ini xor===============')
hasil = a ^ a
print('Nilai',a,'xor',a,'adalah',hasil)
hasil = a ^ b
print('Nilai',a,'xor',b,'adalah',hasil)
hasil = b ^ a
print('Nilai',b,'xor',a,'adalah',hasil)
hasil = b ^ b
print('Nilai',b,'xor',b,'adalah',hasil)

print('\n===============Ini nand===============')
hasil = not (a and a)
print('Nilai',a,'nand',a,'adalah',hasil)
hasil = not (a and b)
print('Nilai',a,'nand',b,'adalah',hasil)
hasil = not (b and a)
print('Nilai',b,'nand',a,'adalah',hasil)
hasil = not (b and b)
print('Nilai',b,'nand',b,'adalah',hasil)

print('\n===============Ini nor===============')
hasil = not (a or a)
print('Nilai',a,'nor',a,'adalah',hasil)
hasil = not (a or b)
print('Nilai',a,'nor',b,'adalah',hasil)
hasil = not (b or a)
print('Nilai',b,'nor',a,'adalah',hasil)
hasil = not (b or b)
print('Nilai',b,'nor',b,'adalah',hasil)

print('\n===============Ini nxor===============')
hasil = a ^ a
print('Nilai',a,'nxor',a,'adalah',not hasil)
hasil = a ^ b
print('Nilai',a,'nxor',b,'adalah',not hasil)
hasil = b ^ a
print('Nilai',b,'nxor',a,'adalah',not hasil)
hasil = b ^ b
print('Nilai',b,'nxor',b,'adalah',not hasil)

print('\n===============Ini xor===============')
a = 5
b = 6
hasil = a ^ a
print('Nilai',a,'xor',a,'adalah',hasil)
hasil = a ^ b
print('Nilai',a,'xor',b,'adalah',hasil)
hasil = b ^ a
print('Nilai',b,'xor',a,'adalah',hasil)
hasil = b ^ b
print('Nilai',b,'xor',b,'adalah',hasil)

print('=============== 1s')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is b
print('a is b =',hasil)

print('\n=============== 1s Not')
a = 5
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is not b =',hasil)
a = 6
b = 6
print('Nilai',a,'memiliki identitas=',hex(id(a)))
print('Nilai',b,'memiliki identitas=',hex(id(b)))
hasil = a is not b
print('a is  not b =',hasil)

print('\n=============== In')
nama = 'Bacharuddin jusuf habibie'

test = 'rud'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'bach'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'ib'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek  = test in nama
print(test,'terdapat di',nama,'adalah '+str(cek))

print('\n=============== In')
data = ['Institut',
        'Teknologi',
        'Bacharuddin',
        'Jusuf',
        'Habibie']
print('Data adalah',data)
test1 = 'Habibie'
test2 = 'Parepare'
test3 = 'kampus'
test4 = 'Institut'

cek = test1 in data
print(test1,'terdapat di data adalah '+str(cek))
cek = test2 in data
print(test2,'terdapat di data adalah '+str(cek))
cek = test3 in data
print(test3,'terdapat di data adalah '+str(cek))
cek = test4 in data
print(test4,'terdapat di data adalah '+str(cek))


# INI OPERATOR BITWISE
a = 27
b = 12
print('\n=============== AND')
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- AND')
c = a & b
print('Nilai',a,'&',b,'biner adalah',format(c,'08b'))

print('\n=============== OR')
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- OR')
c = a | b
print('Nilai',a,'|',b,'biner adalah',format(c,'08b'))


print('\n=============== not In')
# tugas buat nama menjadi nama lengkap masing masing
nama = 'Desvi'

test = 'rud'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'bach'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'ib'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'a'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'i'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'u'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'e'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

test = 'o'
cek  = test not in nama
print(test,'tidak terdapat di',nama,'adalah '+str(cek))

print('\n=============== not In')
# tugas dengan cara yang sama buat operator untuk not in
data = ['Desvi']
print('Data adalah',data)
test1 = 'Desvi'
test2 = 'Des'
test3 = 'vi'
test4 = 'Desvi'

cek = test1 not in data
print(test1,'tidak terdapat di data adalah '+str(cek))
cek = test2 not in data
print(test2,'tidak terdapat di data adalah '+str(cek))
cek = test3 not in data
print(test3,'tidak terdapat di data adalah '+str(cek))
cek = test4 not in data
print(test4,'tidak terdapat di data adalah '+str(cek))

print('\n=============== XOR')
#tugas untuk operator XOR, c = a ^ b
a = 27
b = 12
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- XOR')
c = a ^ b
print('Nilai',a,'^',b,'biner adalah',format(c,'08b'))

print('\n=============== not')
#tugas untuk operator not, c = ~a
a = 27
b = 12
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- not')
c = ~a
print('Nilai',~a,'biner adalah',format(c,'08b'))

print('\n=============== not')
#tugas untuk operator not, c = ~b
a = 27
b = 12
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- not')
c = ~b
print('Nilai',~b,'biner adalah',format(c,'08b'))

print('\n=============== geser kanan')
#tugas untuk operator geser kanan, c = a >> 2
a = 27
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('--------------------------------------------- geser kanan')
c = a >> 2
print('Nilai',(a) >> 2,'biner adalah',format(c,'08b'))

print('\n=============== geser kiri')
#tugas untuk operator geser kiri, c = a << 2
a = 27
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('--------------------------------------------- geser kiri')
c = a >> 2
print('Nilai',(a) << 2,'biner adalah',format(c,'08b'))

print('\n=============== not and')
#tugas untuk operator not and, c = ~(a & b)
a = 27
b = 12
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- not and')
c = ~(a & b)
print('Nilai',~(a & b),'biner adalah',format(c,'08b'))

print('\n=============== not or')
#tugas untuk operator not or, c = ~(a | b)
a = 27
b = 12
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- not or')
c = ~(a | b)
print('Nilai',~(a | b),'biner adalah',format(c,'08b'))

print('\n=============== not xor')
#tugas untuk operator not xor, c = ~(a ^ b)
a = 27
b = 12
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('Nilai',b,'dalam biner    = ',format(b,'08b'))
print('--------------------------------------------- not xor')
c = ~(a ^ b)
print('Nilai',~(a ^ b),'biner adalah',format(c,'08b'))

print('\n=============== not geser kanan')
#tugas untuk operator not geser kanan, c = ~(a >> 2)
a = 27
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('--------------------------------------------- not geser kanan')
c = ~(a >> 2)
print('Nilai',~((a) >> 2),'biner adalah',format(c,'08b'))

print('\n=============== not geser kiri')
#tugas untuk operator not geser kanan, c = ~(a << 2)
a = 27
print('Nilai',a,'dalam biner    = ',format(a,'08b'))
print('--------------------------------------------- not geser kanan')
c = ~(a << 2)
print('Nilai',~((a) << 2),'biner adalah',format(c,'08b'))
























































      
      























