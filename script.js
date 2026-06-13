async function loadFixtures(){

const response = await fetch('fixtures.csv');

const csv = await response.text();

const rows = csv.split('\n').slice(1);

const tbody =
document.querySelector('#fixtureTable tbody');

tbody.innerHTML='';

rows.forEach(row=>{

const cols=row.split(',');

if(cols.length<4) return;

const tr=document.createElement('tr');

tr.innerHTML=`
<td>${cols[0]}</td>
<td>${cols[1]}</td>
<td>${cols[2]}</td>
<td>${cols[3]}</td>
`;

tbody.appendChild(tr);

});

}

loadFixtures();
