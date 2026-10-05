# Try three examples

[English](README.md) · [中文](README.zh.md) · [Français](README.fr.md) · [Español](README.es.md) · [Italiano](README.it.md) · [Deutsch](README.de.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

These inputs are synthetic teaching examples, not experimental evidence. The tutorial previews demonstrate separate product workflows; they are not outputs generated from these example inputs.

## Conceptual sample preparation · Illustration

### Input

Create a conceptual illustration with three labeled panels: collect sample, prepare sample, observe sample. White background, blue-green palette, clear left-to-right arrows. No invented instruments, values or biological mechanisms. Label it “conceptual teaching example”.

### Steps and checks

Use the prompt in Illustration. Review labels and arrow direction, then try one editing tool shown in the tutorial. The example does not specify a real experimental protocol.

[See the complete workflow](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-illustration-tutorial.mp4)

## Synthetic measurements over time · DataChart

### Input

[synthetic-timeseries.csv](datachart/synthetic-timeseries.csv)

### Steps and checks

Upload the CSV in DataChart. Plot signal_a and signal_b against time_min as two series, with time_min on the horizontal axis. Label the vertical axis “arbitrary units”; compare every point with the CSV. Inspect the legend and export using the options available in your workflow.

[See the complete workflow](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-datachart-tutorial.mp4)

## A teaching data-review workflow · FlowChart

### Input

Create a teaching workflow: receive synthetic dataset → validate column names and units → review missing values → summarize → review chart → share. If validation fails, return to the input. Label the decision branches and keep the review step before sharing.

### Steps and checks

Use the workflow text in FlowChart. Inspect each node, the validation loop and the decision labels. Change one node in the editor, then check that the relationships still match the input.

[See the complete workflow](https://cdn.scifig.ai/images/media-kit/2026-10/videos/v4-flowchart-tutorial.mp4)

Review scientific meaning, labels and sources before sharing. Editing and export options depend on the workspace and workflow; the tutorials show specific examples.

SciFig is a commercial platform. This repository is a public resource hub, not the product source code. Media, templates and the MIT-licensed Skill have separate terms; none grants blanket rights to the other materials.

[Licenses and usage](../docs/example-usage.md)
