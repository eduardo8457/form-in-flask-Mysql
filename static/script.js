
var opt_1 = new Array("-", "Front-end", "Back-end", "Mobile");
var opt_2 = new Array("-", "ingles", "Português", "Espanhol");
var opt_3 = new Array("-", "Java","JavaScript","PHP");
var opt_4 = new Array("-", "Vue.js", "Spring", "Laravel");


function menuDinamico() {
    var Departamento;
    Departamento = document.formulario1.Departamento[document.formulario1.Departamento.selectedIndex].value;
    if (Departamento != 0) {
        mis_opts = eval("opt_" + Departamento);
        num_opts = mis_opts.length;
        document.formulario1.dinamico.length = num_opts;

        for (i = 0; i < num_opts; i++) {
            document.formulario1.dinamico.options[i].value = mis_opts[i];
            document.formulario1.dinamico.options[i].text = mis_opts[i];
        }
    } else {
        document.formulario1.dinamico.length = 1;
        document.formulario1.dinamico.options[0].value = "-";
        document.formulario1.dinamico.options[0].text = "-";
    }
    document.formulario1.dinamico.options[0].selected = true;

}
