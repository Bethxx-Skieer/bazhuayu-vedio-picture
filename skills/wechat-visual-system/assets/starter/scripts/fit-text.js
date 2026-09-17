function fitSingleLine(element) {
  const baseline = Number.parseFloat(getComputedStyle(element).fontSize);
  const minimum = Number.parseFloat(element.dataset.minSize || "24");
  const fits = () =>
    element.scrollWidth <= element.clientWidth + 0.5 &&
    element.scrollHeight <= element.clientHeight + 0.5;

  element.style.fontSize = `${baseline}px`;
  if (fits()) return;

  let low = minimum;
  let high = baseline;
  while (high - low > 0.5) {
    const middle = (low + high) / 2;
    element.style.fontSize = `${middle}px`;
    if (fits()) low = middle;
    else high = middle;
  }
  element.style.fontSize = `${Math.max(minimum, low)}px`;
}

function fitTextBlock(element) {
  const baseline = Number.parseFloat(getComputedStyle(element).fontSize);
  const minimum = Number.parseFloat(element.dataset.minSize || "24");
  const container = element.parentElement;
  const fits = () =>
    element.scrollWidth <= container.clientWidth + 0.5 &&
    element.scrollHeight <= container.clientHeight + 0.5;

  element.style.fontSize = `${baseline}px`;
  if (fits()) return;

  let low = minimum;
  let high = baseline;
  while (high - low > 0.5) {
    const middle = (low + high) / 2;
    element.style.fontSize = `${middle}px`;
    if (fits()) low = middle;
    else high = middle;
  }
  element.style.fontSize = `${Math.max(minimum, low)}px`;
}

async function fitRegisteredText() {
  if (document.fonts?.ready) await document.fonts.ready;
  document.querySelectorAll("[data-fit-text]").forEach(fitSingleLine);
  document.querySelectorAll("[data-fit-block]").forEach(fitTextBlock);
  document.documentElement.dataset.textFitReady = "true";
}

if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", fitRegisteredText, { once: true });
} else {
  fitRegisteredText();
}
