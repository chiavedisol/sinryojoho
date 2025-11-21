import jsPDF from "jspdf";
import html2canvas from "html2canvas";

export async function generatePDF(text: string) {
    // Create a temporary div for rendering
    const element = document.createElement("div");
    element.style.position = "absolute";
    element.style.left = "-9999px";
    element.style.top = "0";
    element.style.width = "210mm"; // A4 width
    element.style.minHeight = "297mm"; // A4 height
    element.style.padding = "20mm";
    element.style.backgroundColor = "white";
    element.style.fontFamily = "\"Times New Roman\", \"YuMincho\", \"Hiragino Mincho ProN\", \"Yu Mincho\", \"MS PMincho\", serif";
    element.style.fontSize = "10.5pt"; // Standard Japanese document font size
    element.style.lineHeight = "1.6";
    element.style.whiteSpace = "pre-wrap";
    element.style.color = "black";

    // Replace newlines with <br> if needed, but white-space: pre-wrap handles it.
    // However, innerText handles it well.
    element.innerText = text;

    document.body.appendChild(element);

    try {
        const canvas = await html2canvas(element, {
            scale: 2, // Higher resolution
            logging: false,
            useCORS: true,
            windowWidth: element.scrollWidth,
            windowHeight: element.scrollHeight
        });

        const imgData = canvas.toDataURL("image/png");
        const pdf = new jsPDF({
            orientation: "portrait",
            unit: "mm",
            format: "a4",
        });

        const imgWidth = 210;
        const pageHeight = 297;
        const imgHeight = (canvas.height * imgWidth) / canvas.width;
        let heightLeft = imgHeight;
        let position = 0;

        pdf.addImage(imgData, "PNG", 0, position, imgWidth, imgHeight);
        heightLeft -= pageHeight;

        while (heightLeft >= 0) {
            position = heightLeft - imgHeight;
            pdf.addPage();
            pdf.addImage(imgData, "PNG", 0, position, imgWidth, imgHeight);
            heightLeft -= pageHeight;
        }

        pdf.save("medical-info.pdf");
    } catch (error) {
        console.error("PDF generation failed:", error);
        alert("PDF生成に失敗しました。");
    } finally {
        document.body.removeChild(element);
    }
}
