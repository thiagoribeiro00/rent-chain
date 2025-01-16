pragma solidity ^0.8.0;

contract Aluguel {
    // Estrutura para representar uma propriedade
    struct Propriedade {
        address locador;
        address locatario;
        uint256 valorAluguel;
        uint256 dataVencimento;
        bool estaAlugada;
    }

    // Mapeamento de propriedades
    mapping(address => Propriedade) public propriedades;

    // Mapeamento de propriedades disponíveis
    mapping(uint256 => address) public propriedadesDisponiveis;

    // Contador de propriedades
    uint256 public contadorPropriedades;

    // Eventos
    event PropriedadeCadastrada(address propriedade);
    event PropriedadeReservada(address propriedade);
    event PagamentoRealizado(address propriedade);

    // Função para cadastrar propriedade
    function cadastrarPropriedade(uint256 _valorAluguel) public {
        require(msg.sender != address(0), "Endereço inválido");
        require(propriedades[msg.sender].locador == address(0), "Propriedade já cadastrada");

        // Cria uma nova propriedade
        propriedades[msg.sender] = Propriedade(
            msg.sender,
            address(0),
            _valorAluguel,
            block.timestamp + 30 days, // Data de vencimento padrão
            false
        );

        // Adiciona à lista de propriedades disponíveis
        propriedadesDisponiveis[contadorPropriedades] = msg.sender;
        contadorPropriedades++;

        emit PropriedadeCadastrada(msg.sender);
    }

    // Função para reservar propriedade
    function reservarPropriedade(address _propriedade) public {
        require(propriedades[_propriedade].locador != address(0), "Propriedade não existe");
        require(propriedades[_propriedade].estaAlugada == false, "Propriedade já alugada");

        // Atualiza o locatário e marca como alugada
        propriedades[_propriedade].locatario = msg.sender;
        propriedades[_propriedade].estaAlugada = true;

        emit PropriedadeReservada(_propriedade);
    }

    // Função para realizar pagamento
    function pagarAluguel(address _propriedade) public payable {
        require(propriedades[_propriedade].locador != address(0), "Propriedade não existe");
        require(propriedades[_propriedade].estaAlugada == true, "Propriedade não alugada");
        require(msg.value >= propriedades[_propriedade].valorAluguel, "Valor insuficiente");

        // Transfere o valor para o locador
        (bool sent, bytes memory data) = payable(propriedades[_propriedade].locador).call{value: msg.value}("");
        require(sent, "Falha ao transferir valor");

        emit PagamentoRealizado(_propriedade);
    }
}
