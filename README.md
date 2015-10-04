# POO2Trabalho0
<meta charset="UTF-8">
Trabalho POO2 – Semestre 20152

Nome: Igor Soares dos Santos, Italo Lourenço Trindade

<h1> Mini Mundo: </h1>

<p>Dois estudantes do IFES foram contratados por jogadores profissionais para desenvolver um simulador do jogo “Age of Empires” , com isso o simulador vai simular uma partida do jogo, ou seja, uma guerra entre as civilizações. 
O jogo basicamente consiste em colocar duas nações uma contra a outra, onde cada nação monta um conjunto de guerreiros para representa-la.
Os guerreiros são divididos em dois grupos os de defesa que são os defensores e os guerreiros de ataque que são os ofensores. </p>
<p>Para esse simulador do jogo, existem 3 possíveis nações a serem escolhidas:</p>
<p>•	China: suas unidades de ataque, em geral, não são muito poderosas. As unidades de defesa têm propriedades bem interessantes.</p>
<p>•	Japão: suas unidades de ataque são poderosas as de defesa nem tanto.</p>
<p>•	Índia: suas unidades de ataque são medianas, mas possuem ótima defesa.</p>
<p>Basicamente serão feitas 4 filas de duelos:</p>
<p>•	1 fila de defesa e 1 de ataque para a nação1</p>
<p>•	1 fila de defesa e 1 de ataque para a nação2</p>
<p>A fila de ataque da nação1 ataca a fila de defesa da nação2.</p>
<p>A fila de ataque da nação2 ataca a fila de defesa da nação1.</p>

<p>A escolha da nação que ataca primeiro é feita por sorteio. Um ataque de uma nação implica em cada ofensor atacar 1 vez. Os ataques são feitos na fila de defensores da nação adversária.</p>
Os ofensores atacarão sucessivamente um defensor até que ele seja eliminado, uma vez que isso ocorra o próximo defensor da fila de defesa entrará em sua vez.</p>
Depois que atacam os ofensores voltam para o final da fila de ofensores.</p>
O jogo acaba se uma nação não tem mais ofensores ou defensores, ou seja, se um fila não tem mais guerreiros a nação perde.</p>
<h5>Desenvolvimento	</h5>
<p>Primeiramente é necessário definir o que é um Guerreiro. Um Guerreiro é alguém que luta, podendo ser ofensor ou defensor e possui obrigatoriamente:</p>
<p>•	Nome</p>
<p>•	Idade</p>
<p>•	Peso</p>
<p>•	Energia: que deve ser inicializada em 100 no momento da criação do guerreiro.</p>
<p>Guerreiros morrem quando sua energia fica menor ou igual a 0.</p>
<p>A habilidade de atacar é definida no ofensor, mas o ofensor não sabe como atacar (sempre será um tipo de ofensor que terá essa habilidade).</p>

<p>A seguir apresentaremos os Guerreiros de cada nação:</p>

<h6>Chineses:</h6>
<p>Ofensores:</p>
<p>1) Chun Ku: os Chun Ku são arqueiros chineses. Retiram 5 pontos de qualquer defensor indiano e 10 pontos de qualquer defensor japonês.</p>
<p>2) Gun Te: os Gun te são guerreiros de grandes espadas. São especialmente bons contra a defesa japonesa, retirando 20 pontos de qualquer defensor. Quando atacam defensores indianos retiram 1 ponto mas morrem em seguida.</p>
<p>3) Nok Tu: os Nok Tu possuem grandes lanças. Retiram 5 pontos de qualquer defensor. Mas a cada ataque geram um Mangal de defesa que é colocado na fila de defensores dos chineses.</p>
<p>Defensores:</p>
<p>1) Mangal de defesa: é um boneco mecânico de defesa automática. Os mangais de defesa retiram 2 pontos de qualquer atacante.</p>
<p>2) Montor do escudo: os montores são guerreiros de grandes escudos cuja energia inicial é de 150 (é o único guerreiro que redefine esse valor). Quando os montores morrem eles levam consigo (matam) o guerreiro ofensor que os atacou.</p>
<p>3) Mirk o conversor: se atacados por Samurais os convertem em guerreiros Gun  Te e colocam na fila de atacantes. Não sofrem qualquer dano de Samurais.</p>

<h6>Japoneses:</h6>
<p>Ofensores:</p>
<p>1) Samurai: guerreiros lendários japoneses. Qualquer defensor atacado perde 50 pontos, exceto Mirk o conversor.</p>
<p>2) Ninja: guerreiros sorrateiros japoneses. Qualquer defensor atacado perde 20 pontos.</p>
<p>Defensores:</p>
<p>1)	Tan tan: os tan tan são guerreiros com escudos fixos nos braços. Quando morrem se transformam em ninjas.</p>

<h6>Indianos:</h6>
<p>Ofensores:</p>
<p>1) Seak: os seak são flexíveis unidades de ataque indianas, possuindo espada e arco. Os Seak retiram 25 pontos de qualquer guerreiro defensor atacado.</p>
<p>Defensores:</p>
<p>1) Monge Leaf: quando atacados por Ninjas ou Chun Kus recebem um escudo de ouro que os tornam inatacáveis por esses tipos de guerreiros ofensores, ou seja, ficam invulneráveis a Ninjas e Chun Kus.</p>
<p>2) Monge Bomb: quando atacados morrem, mas deixam o ofensor atacante com energia em 1 unidade.</p>
<p>3) Monge Barrier: quando morre coloca 2 monges barrier em seu lugar com metade da energia. Ou seja, 1 Monge Barrier de 100 se transforma em 2 de 50, esses 2 em 4 de 25, esses em 8 de 12 que por sua vez viram 16 de 6, depois 32 de 3, 64 de 1 e daí quando atacados morrem de vez.</p>
<p>O programa deverá ler 2 arquivos (nacao1.txt e nacao2.txt) e montar as filas de ofensores e defensores de cada nação.</p>
<p>Entrada de dados:</p>
<p>A entrada de dados de um arquivo de nação deverá ter o seguinte formato:</p>
<p><nome da nação></p>
<p>Ofensores:</p>
(tipo do ofensor)(nome do ofensor)(idade 1 )(peso 1)
<p>...</p>
(tipo do ofensor n)(nome do ofensor)(idade n)(peso n)
<p>Defensores:</p>
(tipo do defensor)(nome do defensor)(idade 1)(peso 1)
<p>...</p>
(tipo do defensor n)(nome do defensor)(idade n)(peso n)
<p>Exemplo:</p>
<p>Japão</p>
<p>Ofensores:</p>
<p>1 NitTe 30 70</p>
<p>1 Fak 24 75</p>
<p>2 Full 23 77</p>
<p>1 Merc 55 80</p>
<p>Defensores:</p>
<p>1 Tark 60 50</p>
<p>1 Lan 40 30</p>
<p>Nesse caso foram criados 3 samurais (NitTe, Fak e Merc), 1 Ninja (Full) e 2 Tan tan (Tark e Lan)</p>
<p>Saída de dados:</p>
<p>A nação vencedora foi: <nome da nação> (Japão, Índia ou China)</p>
<p>A nação perdedora foi: <nome da nação> (Japão, Índia ou China)</p>
<p>Acabaram os guerreiros <categoria> (Ofensores ou defensores).
<p>Exemplo:</p>
<p>A nação vencedora foi: Japão</p>
<p>A nação perdedora foi: Índia</p>
<p>Acabaram os guerreiros Defensores.</p>

	

