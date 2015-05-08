
sequence_1 = raw_input('Sequence 1: ')
sequence_2 = raw_input('Sequence 2: ')


list = ['A', 'T', 'G', 'C']

for c in sequence_1 + sequence_2:
    if list.count(c) == 0:
        print 'Please enter valid DNA nucleotides: A, T, G, or C'
    else:
        print 'Please proceed'

        while True:
            modification = raw_input('What do you want to do:\
                                        a (add indel)\
                                        d (delete indel)\
                                        s (score)\
                                        q (quit): ')
            
            a = "a"
            while True:
                if modification.find("a") != -1:
                    choose_sequence = int(raw_input('Work on which sequence (1 or 2): '))
                
                    if choose_sequence == 1:
                        choose_index = int(raw_input('Before which index: '))
                        sequence_1 = sequence_1.replace(sequence_1[choose_index], "-" + sequence_1[choose_index])
                        break
                    elif choose_sequence == 2:
                        choose_index = int(raw_input('Before which index: '))
                        sequence_2 = sequence_2.replace(sequence_2[choose_index], "-" + sequence_2[choose_index])
                        break
                    else:
                        print "Please choose between 1 or 2."

            d = "d"
            while True:
                if modification.find("d") != -1:
                    choose_sequence = int(raw_input('Work on which sequence (1 or 2): '))

                    if choose_sequence == 1:
                        choose_index = int(raw_input('Before which index: '))
                        sequence_1 = sequence_1.replace(sequence_1[choose_index], "")
                        break
                    elif choose_sequence == 2:
                        choose_index = int(raw_input('Before which index: '))
                        sequence_2 = sequence_2.replace(sequence_2[choose_index], "")
                        break
                    else:
                        print "Please choose between 1 or 2."
            
                
                
                

       


