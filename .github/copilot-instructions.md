# Descrição do Projeto

Este projeto é um site educacional para compartilhar tarefas de casa e exercícios de programação com estudantes. Os estudantes podem navegar, visualizar e baixar tarefas diretamente do portal.

## Estrutura do Projeto

- [`assignments/`](../assignments/) Cada tarefa de casa é armazenada em sua própria subpasta com uma estrutura consistente.
- [`templates/`](../templates/) Templates reutilizáveis para novo conteúdo
- [`assets/`](../assets/) Contém os recursos do site incluindo CSS, JavaScript, imagens e arquivos de configuração
- [`index.html`](../index.html) A página principal do site que serve como um portal estático para navegar e visualizar tarefas. O conteúdo é configurável através do arquivo [`config.json`](../config.json) para gerar dinamicamente listas e detalhes de tarefas.

## Diretrizes do Projeto

- Manter estilo consistente em todas as páginas
- Manter nomes de arquivos e pastas descritivos e organizados

## Padrões Educacionais

Ao gerar conteúdo para este projeto:

- **Focado em aprendizado**: Todo conteúdo deve ser projetado com objetivos de aprendizado claros e níveis de dificuldade apropriados
- **Amigável para estudantes**: Use linguagem clara e encorajadora que motiva os estudantes

## Padrão de Commits

Este projeto utiliza o padrão **Conventional Commits** para mensagens de commit. Siga este padrão ao criar commits para garantir clareza e automação nos processos de versionamento e integração contínua.

### Formato

```
<tipo>[escopo opcional]: <descrição>
```

- **tipo**: fix, feat, docs, style, refactor, test, chore, etc.
- **escopo**: (opcional) área do código afetada, entre parênteses.
- **descrição**: breve descrição da mudança, no imperativo.

### Exemplos

- `feat(assignments): adicionar nova tarefa de Python`
- `fix(config): corrigir data de entrega da tarefa de análise de dados`
- `docs(readme): atualizar instruções de configuração`
- `style(css): ajustar espaçamento dos cards de tarefas`
- `refactor(js): simplificar função de carregamento de tarefas`
- `test(api): adicionar testes para endpoint de tarefas`
- `chore(deps): atualizar dependências do projeto`

Para mais detalhes, consulte: [Conventional Commits](https://www.conventionalcommits.org/pt-br/v1.0.0/)