#Dado o texto abaixo, imprima uma lista com as palavras encontradas e a quantidade de vezes que ela aparece. https://www.lipsum.com/feed/html (usar dicionário).

lista = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed nec massa a ex maximus sodales. Proin orci erat, consequat ac euismod eget, auctor et risus. Ut accumsan, sapien at mollis efficitur, nibh magna ullamcorper tellus, ac tristique mi massa eu dolor. Suspendisse sit amet turpis sit amet metus tincidunt porta vel vitae purus. Sed sit amet porta lacus. Etiam ultricies volutpat leo, quis blandit justo hendrerit a. Ut iaculis porttitor elit, eget aliquam dui auctor quis. Sed suscipit vitae mauris quis luctus. Donec id ligula vitae orci molestie efficitur. Mauris id lectus dolor. Nullam ipsum ex, eleifend non tristique at, consequat eget velit. In quis facilisis velit. Duis pharetra massa eu dolor viverra, ac vulputate ipsum molestie. Donec ornare tincidunt leo eget finibus. Proin a gravida lorem.

Curabitur accumsan ullamcorper dui sit amet luctus. Fusce vulputate ullamcorper nibh a sollicitudin. Duis eu arcu non dolor dignissim vestibulum. Maecenas faucibus a mi nec tempor. Nulla volutpat ac ante et ultricies. Nunc sollicitudin nisi eget sagittis posuere. Vivamus dapibus felis turpis, id tincidunt massa cursus quis. Suspendisse vitae velit bibendum, dictum tellus et, tincidunt metus. Maecenas ornare, turpis quis dapibus pellentesque, arcu orci sagittis sapien, vel posuere erat nisl in justo. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed non dignissim ligula. Duis pretium imperdiet urna quis tincidunt.

Phasellus ultrices tristique urna quis efficitur. Praesent fringilla maximus lorem nec tincidunt. Etiam sapien magna, euismod in tellus eget, euismod faucibus massa. Integer blandit enim feugiat nulla suscipit, ut rhoncus lorem interdum. Phasellus et diam ut enim finibus sodales consequat varius magna. Pellentesque laoreet lacus mi, quis lobortis eros facilisis nec. In vitae justo at nisl consectetur tincidunt quis efficitur nulla. Vivamus fermentum mauris non nulla mollis, ac blandit sapien euismod. Mauris vel lorem fermentum, laoreet odio et, facilisis leo. Curabitur mauris sapien, lobortis quis rhoncus eu, vulputate sit amet nisi. Mauris sollicitudin augue justo, nec efficitur massa tincidunt ac. Pellentesque mattis vestibulum dui, sed tempus magna pulvinar sed. Fusce ut ante mauris. Proin vitae sem fringilla, tristique nisl eget, volutpat lectus. Nulla ornare nulla ac leo convallis tempor.

Aliquam nec nibh metus. Nam vel blandit odio. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Sed vulputate metus vel lobortis congue. Sed dapibus elementum magna, pharetra maximus dui elementum sed. Donec et semper lorem, sit amet lobortis orci. Vestibulum at elementum leo. Curabitur quis arcu non velit hendrerit accumsan. Nulla semper tellus vitae nisi volutpat, at finibus lectus sollicitudin. Vivamus efficitur mi rutrum orci porta tempor pretium in est. Aenean eget ipsum aliquet, dictum mauris at, auctor libero. Vivamus eget scelerisque massa, placerat scelerisque leo. Nullam tempor pharetra ipsum non ornare. Fusce consequat quis est sed feugiat.

Maecenas viverra nibh dolor, eu interdum ante tempor quis. Donec commodo fringilla odio vel tincidunt. Duis bibendum orci eget condimentum aliquam. Curabitur fringilla in lorem nec rutrum. Quisque non massa faucibus, venenatis ante eu, elementum enim. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Fusce id odio eu purus semper vehicula. Maecenas lacus tortor, pretium eget nibh vel, viverra consequat augue. In accumsan vestibulum facilisis. Sed dapibus turpis sodales varius laoreet. Quisque pretium sapien sit amet ante feugiat, non faucibus metus bibendum. Phasellus bibendum, nunc eu fermentum mattis, metus elit auctor nunc, vel ornare risus nunc faucibus dolor. Phasellus posuere nulla ac convallis pulvinar. Nullam ullamcorper ipsum ac nunc finibus sodales.'''

nova = lista.replace('.','')
nova2 = nova.replace(',','')
nova3 = nova2.split(' ')
quantidade = {}

for c in nova3:
    quanti = 0
    if nova3.count(c) > 1 and nova3.count(c) not in quantidade:
        quanti = nova3.count(c)
        quantidade[c] = quanti
print(quantidade)
