# FlexOrder-DesignPatterns

Refiz o sistema legado, aplicando os padrões propostos no desafio

Transformei a classe monolítica em um sistema modular, de fácil manutenção e seguindo os princípios SOLID

Strategy ( Estrategias ) para pagamento e frete
Decorator ( Decorators ) para desconto e taxas
Facade para o checkout

Strategy define o tipo de pagamento e frete, facilitando remoções e adicições de tipos de frete
Decorator adiciona os descontos e taxas dinamicamente, evitando modificações no codigo base
Facade simplifica o processo de checkout