const tables = document.querySelectorAll("table");
const result = [];
i = 0;
tables.forEach((table) => {
    // if (i == 0) {
        const rows = table.querySelectorAll("tr");
        const td_data = [];

        rows.forEach((row) => {
            const cells = row.querySelectorAll("td");
            // const cell = cells;
            for (let index = 0; index < cells.length; index++) {
                if (cells[index] && cells[index].textContent.trim() != " ") {
                    td_data.push(cells[index].textContent.trim())
                }
            }
            // if (cell) {
            //     column.push(
            //         cell.textContent.replace("\n", "").replace("\n", "")
            //     );
            // }
        });

        result.push(td_data);
    // }
});
// }

const jsonResult = JSON.stringify(result);

console.log(jsonResult);
jss=JSON.parse(jsonResult)

gp=["گروه بانک"
,"گروه رایانه"
,"گروه زراعت"
,"گروه املاک"
,"گروه سرمایه گذاری"
,"گروه مخابرات"
,"گروه محصولات شیمیایی"
,"گروه حمل و نقل"
,"گروه ماشین آلات و تجهیزات"
,"گروه سیمان،آهک"
,"گروه منسوجات"
,"گروه قند و شکر"
,"گروه فرآوردهای نفتی"
,"گروه بیمه"
,"گروه عرضه برق و آب"
,"گروه محصولات غذایی"
,"گروه واسطه گری مالی"
,"گروه خدمات فنی ومهندسی"
,"گروه سایرمحصولات کانی غیرفلزی"
,"گروه هتل و رستوران"
,"گروه ماشین آلات و دستگاه های برقی"
,"گروه استخراج کانه های فلزی"
,"گروه فعالیت های کمکی به نهادهای مالی واسط"
,"گروه کاشی و سرامیک"
,"گروه ساخت دستگاه ها و وسایل ارتباطی"
,"گروه لاستیک و پلاستیک"
,"گروه اطلاعات و ارتباطات"
,"گروه سایر تجهیزات حمل و نقل"
,"گروه استخراج نفت و گاز"
,"گروه خودرو و ساخت قطعات"
,"گروه فعالیت های هنری و سرگرمی"
,"گروه چندرشته ای"
,"گروه تولید محصولات کامپیوتری"
,"گروه ساخت محصولات فلزی"
,"گروه پیمانکاری صنعتی"
,"گروه محصولات چوبی"
,"گروه استخراج زغال"
,"گروه محصولات کاغذی"
,"گروه دباغی"
,"گروه خرده فروشی"
,"گروه انتشار"
,"گروه صندوق سرمايه گذاري قابل معامله"
]

njs=[]
for (let i = 0; i < gp.length; i++) {
  njs.push({'group':gp[i],'symbol':jss[i]})
}
