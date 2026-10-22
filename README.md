# 产品经理作品集 · Product Artifacts
[![tests](https://github.com/lechangxu/product-artifacts/actions/workflows/tests.yml/badge.svg)](https://github.com/lechangxu/product-artifacts/actions/workflows/tests.yml)

公开的产品文档样本：两份真实产品的 PRD 摘编、一份变更记录、一个开源数据产品的索引。
用来展示怎么定义问题、怎么把需求写成可验收的规则，而不是展示代码。

## 这是什么 / 不是什么

- **是**：从真实私有仓里摘出来的产品文档 —— 保留了问题定义、用户画像、关键决策与生成约束，
  删掉了内部路径、接口契约、源码与截图。
- **是**：可对照阅读的两版 PRD —— v2.0 是概念期（要不要做、给谁做），v4.8 是执行期（怎么判定学会了）。
- **不是**：源码仓库、演示环境或客户案例。涉及合作方的文档一律不发，业务能力用虚构案例另行展示。

## 目录

| 文件 | 内容 |
| :---- | :---- |
| [readleap/prd-v2.0.md](readleap/prd-v2.0.md) | ReadLeap Max PRD 摘编 v2.0：问题、用户、核心流程、MVP 边界 |
| [readleap/prd-v4.8.md](readleap/prd-v4.8.md) | ReadLeap Max PRD 摘编 v4.8：自适应测评、AI 生成约束（防幻觉）、指标与路线图 |
| [readleap/CHANGELOG.md](readleap/CHANGELOG.md) | 20 个版本的演进记录：每个版本改的是哪条产品决策 |
| [queryweb3/README.md](queryweb3/README.md) | QueryWeb3（Polkadot 生态数据产品）PRD 与里程碑验收清单的入口 |
| [LICENSE](LICENSE) | MIT |
| [README.md](README.md) | 本文件：这是什么/不是什么、每份文档怎么读、局限 |

## 示例输出（真实文档片段）

以下是本仓 readleap/prd-v4.8.md §5 的原文摘录，未改写：

1. **关注点分离**：PRD 定义约束与验收法则；提示词注册表维护精确英文 prompt；代码库为执行唯一真相源，1:1 映射。
2. **写作者必须物理写入**：目标词必须真实出现在正文里，不允许只在结构化字段里返回；文章长度有硬性下限。
3. **审核者必须物理核验**：像正则匹配一样对正文做子串校验，缺一个目标词或篇幅不足就无条件驳回。
4. **判卷不泄露答案**：除保底模式外绝不直接给答案；判卷依据 100% 来自原文，不引入外部知识。
5. **批改不捏造错误**：句子本身正确就保持原样，禁止为了显得有用而改。

## 怎么读

1. **只想看产品判断力**：读两份 PRD 的「关键决策 / 生成约束」两节 —— 它们回答的是
   「为什么这么定」，而不是「页面长什么样」。
2. **想看迭代能力**：读 CHANGELOG，按版本号顺序看同一模块怎么被反复修正
   （例如掌握判定：单阈值 → 多信号 → 五因子证据模型）。
3. **想看 B 端/Grant 交付**：看 queryweb3 目录，它指向公开仓里的 PRD 与逐项验收清单。

## 仓结构与工具

| 项 | 内容 |
| :---- | :---- |
| 文档格式 | Markdown |
| 代码 | 仅一个链接校验器 |
| 运行时依赖 | 无（只用标准库） |
| 校验 | `scripts/check_links.py` |
| 测试 | unittest，5 个用例 |
| CI | GitHub Actions，Python 3.11 + 3.12 |

## 局限

- 所有摘编都是**删减版**：删掉的部分不影响结论，但会让你看不到完整推导过程。
- 文档中的目标值（留存、时长、NPS 等）是**设计目标**，不是实测数据；本项目未公开经营数据。
- ReadLeap Max 的代码仓保持私有，本仓不含可运行实现。

## License

MIT，见 [LICENSE](LICENSE)。
