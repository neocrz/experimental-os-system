function formataValorCpf(campo) {
    var vr = campo.value;
    vr = vr.replace(/\D/g, ''); // Remove todos os caracteres não numéricos

    var tam = vr.length;
    if (tam <= 3) {
        campo.value = vr;
    } else if (tam > 3 && tam <= 6) {
        campo.value = vr.substr(0, 3) + '.' + vr.substr(3, tam - 3);
    } else if (tam > 6 && tam <= 9) {
        campo.value = vr.substr(0, 3) + '.' + vr.substr(3, 3) + '.' + vr.substr(6, tam - 6);
    } else if (tam > 9 && tam <= 11) {
        campo.value = vr.substr(0, 3) + '.' + vr.substr(3, 3) + '.' + vr.substr(6, 3) + '-' + vr.substr(9, tam - 9);
    } else {
        campo.value = vr.substr(0, 3) + '.' + vr.substr(3, 3) + '.' + vr.substr(6, 3) + '-' + vr.substr(9, 2);
    }
};


    function formataValorRg(campo) {
        var vr = campo.value;
        if (vr.length > 0) {
            vr = vr.replace(/\D/g, ''); // Remove todos os caracteres não numéricos
        }

        var tam = vr.length;
        if (tam <= 2) {
            campo.value = vr;
        } else if (tam > 2 && tam <= 5) {
            campo.value = vr.substr(0, 2) + '.' + vr.substr(2, tam - 2);
        } else if (tam > 5 && tam <= 8) {
            campo.value = vr.substr(0, 2) + '.' + vr.substr(2, 3) + '.' + vr.substr(5, tam - 5);
        } else if (tam > 8) {
            campo.value = vr.substr(0, 2) + '.' + vr.substr(2, 3) + '.' + vr.substr(5, 3) + '-' + vr.substr(8, tam - 8);
        }
    };

    function formataTelefone(campo) {
        var vr = campo.value;
        if (vr.length > 0) {
            vr = vr.replace(/\D/g, ''); // Remove todos os caracteres não numéricos
        }

        var tam = vr.length;
        if (tam <= 2) {
            campo.value = vr;
        } else if (tam > 2 && tam <= 7) {
            campo.value = '(' + vr.substr(0, 2) + ') ' + vr.substr(2, tam - 2);
        } else if (tam > 7 && tam <= 11) {
            if (tam === 8) {
                campo.value = '(' + vr.substr(0, 2) + ') ' + vr.substr(2, 4) + '-' + vr.substr(6, 2);
            } else if (tam === 9) {
                campo.value = '(' + vr.substr(0, 2) + ') ' + vr.substr(2, 5) + '-' + vr.substr(7, 2);
            } else if (tam === 10) {
                campo.value = '(' + vr.substr(0, 2) + ') ' + vr.substr(2, 4) + '-' + vr.substr(6, 4);
            } else if (tam === 11) {
                campo.value = '(' + vr.substr(0, 2) + ') ' + vr.substr(2, 5) + '-' + vr.substr(7, 4);
            }
        } else if (tam > 11) {
            campo.value = '(' + vr.substr(0, 2) + ') ' + vr.substr(2, 5) + '-' + vr.substr(7, 4);
        }
    };

    function formataValorCnpj(campo) {
        var vr = campo.value;
        vr = vr.replace(/\D/g, ''); // Remove todos os caracteres não numéricos

        var tam = vr.length;
        if (tam <= 2) {
            campo.value = vr;
        } else if (tam > 2 && tam <= 5) {
            campo.value = vr.substr(0, 2) + '.' + vr.substr(2, tam - 2);
        } else if (tam > 5 && tam <= 8) {
            campo.value = vr.substr(0, 2) + '.' + vr.substr(2, 3) + '.' + vr.substr(5, tam - 5);
        } else if (tam > 8 && tam <= 12) {
            campo.value = vr.substr(0, 2) + '.' + vr.substr(2, 3) + '.' + vr.substr(5, 3) + '/' + vr.substr(8, tam - 8);
        } else if (tam > 12 && tam <= 14) {
            campo.value = vr.substr(0, 2) + '.' + vr.substr(2, 3) + '.' + vr.substr(5, 3) + '/' + vr.substr(8, 4) + '-' + vr.substr(12, tam - 12);
        } else {
            campo.value = vr.substr(0, 2) + '.' + vr.substr(2, 3) + '.' + vr.substr(5, 3) + '/' + vr.substr(8, 4) + '-' + vr.substr(12, 2);
        }
    };

    function formataValorData(campo) {
        var vr = campo.value;
        vr = vr.replace(/\D/g, '');// Remove todos os caracteres não numéricos
    
        var tam = vr.length;
        if (tam <= 2) {
            campo.value = vr
        } else if (tam > 2 && tam <= 4) {
            campo.value = vr.substr(0, 2) + '/' + vr.substr(2, tam - 2);
        } else if (tam > 4 && tam <= 8) {
            campo.value = vr.substr(0, 2) + '/' + vr.substr(2, 2) + '/' + vr.substr(4, tam - 4);
        } else {
            campo.value = vr.substr(0, 2) + '/' + vr.substr(2, 2) + '/' + vr.substr(4, 4);
        }
    }

    function formataValorPreco(campo) {
        var vr = campo.value;
        vr = vr.replace(/\D/g, ''); // Remove todos os caracteres não numéricos
        
        var tam = vr.length;
        if (tam <= 2) {
            campo.value = '0,' + vr;
        } else {
            if (vr.startsWith('0')) {
                vr = vr.slice(1); // Retorna 'vr' sem o zero inicial
            }
            var inteiro = vr.substr(0, tam - 2);
            var decimal = vr.substr(tam - 2, 2);
            campo.value = inteiro + ',' + decimal;
        }
    }

    function formataValorCep(campo) {
        var vr = campo.value;
        if (vr.length > 0) {
            vr = vr.replace(/\D/g, ''); // Remove todos os caracteres não numéricos
        }

        var tam = vr.length;
        if (tam <= 5) {
            campo.value = vr;
        } else if (tam > 5) {
            campo.value = vr.substr(0, 5) + '-' + vr.substr(5, 3);
        }
    };

    function TrataPaste(este, e, tipo){
        var texto = e.clipboardData.getData('text').replace(new RegExp("\\.","gm"), "").replace("-", "").replace("/", "");
        var isnum = /^\d+$/.test(texto);
        debugger;
        
        if (isnum == false){
            e.preventDefault();
            return;

        }
        var caixa = document.getElementById(tipo);
        teste.value = texto;
        
        switch(tipo){
            case 'cpf':
            formataValorCpf(caixa);
            break;
            case 'cnpj':
            formataValorCnpj(caixa);
            break;
            case 'cep':
            formataValorCep(caixa);
            break;
            case 'rg':
            formataValorRg(caixa);
            break;
            case 'tel':
            formataTelefone(caixa);
            break;
            case 'data':
            formataValorData(caixa);
            break;
            case 'preco':
                formataValorPreco(caixa);
            break;
        }
        
        e.preventDefault();
    };
