(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[408],{7689:function(e,t,n){(window.__NEXT_P=window.__NEXT_P||[]).push(["/summoners/[region]/[summoner]/champions",function(){return n(3535)}])},41721:function(e,t,n){"use strict";n.d(t,{Bp:function(){return m},Td:function(){return s},dC:function(){return c}});var i=n(82729),a=n(16829),l=n(13247),r=n(43671);function o(){let e=(0,i._)(["\n  table-layout: auto;\n  width: 100%;\n  border-radius: ",";\n\n  thead th {\n    &:first-of-type {\n      border-radius: ",";\n    }\n    &:last-of-type {\n      border-radius: ",";\n    }\n  }\n  tbody {\n    tr:last-of-type {\n      td {\n        &:first-of-type {\n          border-radius: ",";\n        }\n        &:last-of-type {\n          border-radius: ",";\n        }\n      }\n    }\n  }\n\n  caption {\n    display: none;\n  }\n\n  th,\n  td {\n    box-sizing: border-box;\n    font-weight: normal;\n    vertical-align: middle;\n    padding: 4px;\n    &:first-of-type {\n      padding-left: 12px;\n    }\n    &:last-of-type {\n      padding-right: 12px;\n    }\n\n    &.adTd {\n      padding: 0 !important;\n    }\n  }\n\n  thead {\n    th,\n    td {\n      position: relative;\n      height: 32px;\n      user-select: none;\n      background: ",";\n      color: ",";\n      font-size: 12px;\n      line-height: 16px;\n      border-bottom: 1px solid;\n      border-color: ",';\n      box-sizing: border-box;\n    }\n  }\n\n  tbody {\n    th,\n    td {\n      text-align: center;\n      &[align="left"] {\n        text-align: left;\n      }\n      &[align="right"] {\n        text-align: right;\n      }\n      border-bottom: 1px solid;\n      border-color: ',";\n    }\n    tr:last-of-type {\n      th,\n      td {\n        border-bottom: 0 none;\n      }\n    }\n    tr:hover {\n      th,\n      td {\n        background: ",";\n      }\n    }\n  }\n\n  .green {\n    color: ",";\n  }\n  .blue {\n    color: ",";\n  }\n  .orange {\n    color: ",";\n  }\n"]);return o=function(){return e},e}let d=a.Z.table(o(),e=>{let{noBorder:t}=e;return t?null:"4px"},e=>{let{noBorder:t}=e;return t?null:"4px 0 0 0"},e=>{let{noBorder:t}=e;return t?null:"0 4px 0 0"},e=>{let{noBorder:t}=e;return t?null:"0 0 0 4px"},e=>{let{noBorder:t}=e;return t?null:"0 0 4px 0"},(0,r.bB)("background","gray100"),(0,r.bB)("color","gray400"),(0,r.bB)("border-color","gray200"),(0,r.bB)("border-color","gray200"),(0,r.bB)("background","gray100"),(0,r.bB)("color","teal500"),(0,r.bB)("color","blue500"),(0,r.bB)("color","orange500")),c=(0,a.Z)("th",{target:"e1tupkk20"})("font-weight:normal;text-align:left;"),s=(0,a.Z)("td",{target:"e1tupkk21"})(l.J.body,";text-align:",e=>{let{align:t}=e;return t||"center"}," !important;font-weight:",e=>{let{variant:t}=e;return"active"===t?"bold":"normal"},";",e=>{let{variant:t}=e,n=(0,r.bB)("color","gray600"),i=(0,r.bB)("background","gray0");return"disabled"===t&&(n=(0,r.bB)("color","gray400")),"active"===t&&(n=(0,r.bB)("color","gray900")),"active"===t&&(i=(0,r.bB)("background","gray100")),"color:".concat(n,"; background: ").concat(i)},"  > *{display:inline-block;vertical-align:middle;}strong{font-size:12px;font-weight:bold;color:",(0,r.bB)("color","gray900"),";}small{font-size:12px;font-weight:normal;color:",(0,r.bB)("color","gray500"),";}"),m=(0,a.Z)("th",{target:"e1tupkk22"})("position:relative;cursor:pointer;font-weight:",e=>{let{variant:t}=e;return"active"===t?"bold !important":"normal"},";color:",e=>{let{variant:t}=e;return"active"===t?(0,r.bB)("color","main600",!0):"inherit"},';&:after{content:"";height:2px;position:absolute;left:0;right:0;bottom:',e=>{let{order:t}=e;return -1===t?"-1px":"auto"},";top:",e=>{let{order:t}=e;return 1===t?"-1px":"auto"},";background:",(0,r.bB)("background","main500"),";display:",e=>{let{variant:t}=e;return"active"===t?"block":"none"},";}text-align:",e=>{let{align:t}=e;return t||"center"},";");t.ZP=d},3535:function(e,t,n){"use strict";n.r(t),n.d(t,{__N_SSP:function(){return ee},default:function(){return et}});var i=n(35944),a=n(67294),l=n(84855),r=n(9008),o=n.n(r),d=n(47937),c=n(33123),s=n(1487),m=n(5152),u=n.n(m),h=n(16829),p=n(8100),g=n(11163),v=n(41664),b=n.n(v),_=n(47631),f=n(39834),Z=n(95367);let y=(0,h.Z)("div",{target:"e1m4iz580"})();function k(e){var t;let{data:n,handleOnClick:r,activeSeasonId:o,isMobileMode:d}=e,{t:c}=(0,l.$G)(["messages"]),s=[];for(let e of Object.keys(n.seasonsById))(null==n?void 0:n.regionSeasons.find(t=>String(t.id)===e))&&s.push(n.seasonsById[e]);let[m,u]=(0,a.useState)(!1),h=()=>{u(!m)},p=e=>()=>{h(),r(e)},g=s.find(e=>e.id===o),v=s.reverse();return(0,i.tZ)(i.HY,{children:(0,i.BX)(y,{children:[(0,i.BX)(Z.eI,{isMobile:d,children:[(0,i.tZ)("label",{htmlFor:"dropdwonSelect",className:"hidden",children:"Select"}),(0,i.tZ)("select",{id:"dropdwonSelect",onChange:e=>{e.preventDefault(),r(Number(e.currentTarget.value))},value:o,children:v.map((e,t)=>{let n=e.is_preseason?c("PRESEASON"):"".concat(c("시즌")," ").concat(e.display_value)+(e.split?" S".concat(e.split):"");return(0,i.tZ)("option",{value:e.id,children:n},"seasonsList_".concat(t))})})]}),!d&&(0,i.tZ)(Z.DZ,{children:(0,i.BX)(f.default,{onOutsideClick:()=>{u(!1)},children:[(0,i.tZ)(Z.Z_,{isOpen:m,onClick:h,hasIcon:!1,children:(0,i.tZ)("span",{children:(null===(t=v[0])||void 0===t?void 0:t.id)===(null==g?void 0:g.id)&&(null==g?void 0:g.is_preseason)?c("PRESEASON"):"".concat(c("시즌")," ").concat(null==g?void 0:g.display_value)+((null==g?void 0:g.split)?" S".concat(null==g?void 0:g.split):"")})}),m&&(0,i.tZ)("div",{children:v.map((e,t)=>{let n=e.is_preseason?c("PRESEASON"):"".concat(c("시즌")," ").concat(e.display_value)+(e.split?" S".concat(e.split):"");return(0,i.tZ)(Z.hP,{type:"button",hasIcon:!1,onClick:p(e.id),children:n},"seasonsList_dropdown_".concat(t))})})]})})]})})}var x=n(40425),N=n(41721),w=n(66199),S=n(43671),E=n(82676),M=n(71074),R=n(87527);let B=[{value:"championsSummonerRank",title:"#"},{value:"name",title:"COMMON_CHAMPION"},{value:"gameWinRate",title:"GAMECOUNT"},{value:"kda",title:"COMMON_KDA"},{value:"scoreGold",title:"COMMON_GOLD"},{value:"scoreCreep",title:"CS"}],T=[{value:"championsSummonerRank",title:"#"},{value:"name",title:""},{value:"gameWinRate",title:"GAMECOUNT"},{value:"kda",title:"COMMON_KDA"},{value:"cs",title:"CS"}],A=[{value:"max_kill",title:"최대 킬"},{value:"max_death",title:"최대 데스"},{value:"scoreDmgDealt",title:"평균 가한 피해량"},{value:"scoreDmgTaken",title:"평균 받은 피해량"},{value:"double_kill",title:"MATCH_MULTIKILL_TWO"},{value:"triple_kill",title:"MATCH_MULTIKILL_THREE"},{value:"quadra_kill",title:"MATCH_MULTIKILL_FOUR"},{value:"penta_kill",title:"MATCH_MULTIKILL_FIVE"}],O=[{value:"RANKED",label:"SUMMONER_MATCH_TYPE_WHOLE"},{value:"SOLORANKED",label:"GLOBAL_QUEUETYPE_RANKED_SOLO_5X5_SHORT"},{value:"FLEXRANKED",label:"SUMMONER_MATCH_TYPE_FLEXRANKED"}],L=[...O,{value:"NORMAL",label:"SUMMONER_MATCH_TYPE_UNRANKED"}];var C=n(24102);let P=(0,h.Z)("div",{target:"eaie9sn0"})("margin-top:12px;/*  컨텐츠 부분 */\n  .content{width:",M.N5,"px;margin:0 auto;}.filter-container{display:flex;align-items:center;}",R.hE,"{margin-left:8px;}thead th{padding:8px 2px;box-sizing:border-box;line-height:inherit;&.word-keep{word-break:keep-all;}}tbody td{color:",(0,S.bB)("color","gray600"),';font-size:12px;&:nth-of-type(n + 4){font-family:"Roboto",sans-serif;}&.rank{color:',(0,S.bB)("color","gray400"),";}.kda{font-size:11px;}.champion-container{display:flex;align-items:center;}.summoner-image{flex-basis:32px;&:hover + .summoner-name a{text-decoration:underline;}a{display:block;width:32px;img{border-radius:50%;}}}.summoner-name{flex:1;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;text-align:left;vertical-align:middle;a{padding:0 6px;color:",(0,S.bB)("color","gray900"),";font-weight:bold;&:hover{text-decoration:underline;}}}}/*  그래프 */\n  .win-ratio{text-align:left;display:flex;align-items:center;justify-content:center;}.winratio-graph{width:90px;position:relative;display:inline-block;height:20px;vertical-align:middle;flex-basis:90px;&.winratio-graph__mobile{width:100%;}}/*  그래프 색 */\n  .winratio-graph__fill{position:absolute;left:0;top:0;height:100%;border-radius:4px;&.left{background:",(0,S.bB)("background","main500"),";border-top-right-radius:0;border-bottom-right-radius:0;z-index:1;&.only-active{border-top-right-radius:4px;border-bottom-right-radius:4px;}}&.right{width:100%;background:",(0,S.bB)("background","red500"),';}}/*  그래프 텍스트 */\n  .winratio-graph__text{position:absolute;top:3px;height:100%;line-height:15px;font-size:11px;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;z-index:1;&.left{left:4px;text-align:left;z-index:1;}&.right{right:4px;text-align:right;}}.text{vertical-align:middle;padding-left:8px;font-weight:normal;flex-basis:38px;box-sizing:border-box;font-family:"Roboto",sans-serif;&.gray{color:',(0,S.bB)("color","gray600"),";}&.red{color:",(0,S.bB)("color","red600"),";}}"),X=(0,h.Z)("div",{target:"eaie9sn1"})("display:flex;align-items:center;justify-content:center;text-align:center;height:205px;p{margin-top:10px;color:",(0,S.bB)("color","gray600"),";font-size:16px;font-weight:normal;}"),I=(0,h.Z)("div",{target:"eaie9sn2"})("height:300px;display:flex;align-items:center;justify-content:center;"),D=(0,h.Z)("strong",{target:"eaie9sn3"})('font-family:"Roboto",sans-serif;color:',e=>{let{kda:t}=e;return Number(t)>=5||"Perfect"===t?(0,S.bB)("color","orange600",!0):5>Number(t)&&Number(t)>=4?(0,S.bB)("color","blue500",!0):4>Number(t)&&Number(t)>=3?(0,S.bB)("color","teal600",!0):(0,S.bB)("color","gray500",!0)},";"),H=(0,h.Z)(N.ZP,{target:"eaie9sn4"})("margin-top:12px;table-layout:fixed;"),F=()=>{let{t:e}=(0,l.$G)("messages");return(0,i.tZ)(X,{children:(0,i.BX)("div",{children:[(0,i.tZ)("div",{className:"Image",children:(0,i.tZ)(x.Z,{width:62,height:62,src:"/static/images/site/common/bg-noData.png",alt:"No data"})}),(0,i.tZ)("p",{children:e("SUMMONER_CHAMPION_TABLE_NO_RESULT")})]})})};function U(e){var t,n,r,o;let{data:c,isMobileMode:s}=e,{t:m}=(0,l.$G)("messages"),{query:{region:u}}=(0,g.useRouter)(),[h]=(0,a.useState)(c.championsById),v=c.regionSeasons[(null==c?void 0:null===(t=c.regionSeasons)||void 0===t?void 0:t.length)-1].id,f=(null===(n=c.most_champions)||void 0===n?void 0:n.season_id)?null===(r=c.most_champions)||void 0===r?void 0:r.season_id:v,[Z,y]=(0,a.useState)(f),[S,M]=(0,a.useState)(!1),[T,O]=(0,a.useState)(!1),[L,X]=(0,a.useState)("RANKED"),[U,K]=(0,a.useState)([]),z="NORMAL"===L||"ARENA"===L,G=Z===v,{data:Y,error:W,isValidating:q,mutate:Q}=(0,p.ZP)("ARENA"===L?[_.Z.node.summoner.summoners.mostChampions.arena(String(u),c.summoner_id),"ARENA",c.summoner_id]:z?[_.Z.node.summoner.summoners.mostChampions.normal(String(u),c.summoner_id),z?"NORMAL":"Normal Not Selected",c.summoner_id]:null,z?e=>(0,C.ZP)({url:e,method:"get"}).then(e=>e.data):null,{fallbackData:c.most_champions,dedupingInterval:0,onSuccess:e=>{let t={},n=e.champion_stats.map((e,n)=>{t={...t,[e.id]:n+1};let i=t[e.id],a=Number(e.win/e.play*100),l=(0,d.XK)(e.kill,e.death,e.assist,e.play),r=Number((e.gold_earned/e.play).toFixed(0)),o=Number(((e.minion_kill+e.neutral_minion_kill)/e.play).toFixed(1)),c=Math.round(o/(e.game_length_second/e.play/60)*10)/10,s=Math.round(r/(e.game_length_second/e.play/60)*10)/10;return{...e,championsSummonerRank:i,name:h[e.id].name,gameWinRate:a,kda:l,scoreGold:r,scoreCreep:o,csPerMin:c,goldPerMin:s}});K(n)}}),{data:V,error:$,isValidating:j,mutate:J}=(0,p.ZP)(z?null:[_.Z.node.summoner.summoners.mostChampions.rank(String(u),c.summoner_id),z?"Normal Selected":L,c.summoner_id,Z],z?null:e=>(0,C.ZP)({url:e,method:"get",params:{game_type:L,season_id:Z}}).then(e=>e.data),{fallbackData:c.most_champions,dedupingInterval:0,onSuccess:e=>{!S&&T&&!e.champion_stats&&G&&(X("NORMAL"),O(!1));let t={},n=e.champion_stats.map((e,n)=>{t={...t,[e.id]:n+1};let i=t[e.id],a=Number(e.win/e.play*100),l=(0,d.XK)(e.kill,e.death,e.assist,e.play),r=Number((e.gold_earned/e.play).toFixed(0)),o=Number(((e.minion_kill+e.neutral_minion_kill)/e.play).toFixed(1)),c=Math.round(o/(e.game_length_second/e.play/60)*10)/10,s=Math.round(r/(e.game_length_second/e.play/60)*10)/10,m=Number((e.damage_dealt_to_champions/e.play).toFixed(0)),u=Number((e.damage_taken/e.play).toFixed(0));return{...e,championsSummonerRank:i,name:h[e.id].name,gameWinRate:a,kda:l,scoreGold:r,scoreCreep:o,csPerMin:c,goldPerMin:s,scoreDmgDealt:m,scoreDmgTaken:u}});K(n)}}),ee=z?Y:V,et=z?W:$,en=z?q:j,ei=z?Q:J;(0,a.useEffect)(()=>{O(!0)},[]),(0,a.useEffect)(()=>{!S&&T&&Z&&ei()},[S,T,Z,ei]);let{data:ea,sort:el,sortType:er}=(0,w.Z)(U,"championsSummonerRank");(0,a.useEffect)(()=>{el(er.key,er.order)},[ee]);let eo=e=>()=>{M(!0),X(e),el("championsSummonerRank",-1)};return(0,i.tZ)(P,{id:"content-container",children:(0,i.BX)("div",{className:"content",children:[(0,i.BX)("div",{className:"filter-container",children:[(0,i.tZ)(k,{data:c,handleOnClick:e=>{"NORMAL"===L&&X("RANKED"),M(!0),y(e),el(er.key,er.order)},activeSeasonId:Z,isMobileMode:s}),(0,i.BX)(R.hE,{children:[(0,i.tZ)(R.ZP,{variant:"RANKED"===L?"primary":null,onClick:eo("RANKED"),children:m("SUMMONER_MATCH_TYPE_WHOLE")}),(0,i.tZ)(R.ZP,{variant:"SOLORANKED"===L?"primary":null,onClick:eo("SOLORANKED"),children:m("GLOBAL_QUEUETYPE_RANKED_SOLO_5X5_SHORT")}),(0,i.tZ)(R.ZP,{variant:"FLEXRANKED"===L?"primary":null,onClick:eo("FLEXRANKED"),children:m("SUMMONER_MATCH_TYPE_FLEXRANKED")}),Z===f&&(0,i.tZ)(R.ZP,{variant:"NORMAL"===L?"primary":null,onClick:eo("NORMAL"),children:m("SUMMONER_MATCH_TYPE_UNRANKED")})]}),Z>=23&&(0,i.tZ)(R.hE,{children:(0,i.tZ)(R.ZP,{variant:"ARENA"===L?"primary":null,onClick:eo("ARENA"),children:m("GLOBAL_QUEUETYPE_ARENA")})})]}),(0,i.BX)(H,{children:[(0,i.tZ)("caption",{children:m("SUMMONER_TITLE_CHAMPION_INFO")}),et?(0,i.tZ)("tbody",{children:(0,i.tZ)("tr",{children:(0,i.tZ)(N.Td,{valign:"middle",children:(0,i.tZ)(F,{})})})}):en?(0,i.tZ)("tbody",{children:(0,i.tZ)("tr",{children:(0,i.tZ)(N.Td,{children:(0,i.tZ)(I,{children:(0,i.tZ)(E.gb,{})})})})}):(null==ee?void 0:null===(o=ee.champion_stats)||void 0===o?void 0:o.length)?(0,i.BX)(i.HY,{children:[(0,i.BX)("colgroup",{children:[(0,i.tZ)("col",{width:"45"}),(0,i.tZ)("col",{width:"auto"}),(0,i.tZ)("col",{width:Z<=2?"90":"140"}),(0,i.tZ)("col",{width:"105"}),(0,i.tZ)("col",{width:"88"}),(0,i.tZ)("col",{width:"72"}),(0,i.tZ)("col",{width:"64"}),(0,i.tZ)("col",{width:"64"}),(0,i.tZ)("col",{width:"66"}),(0,i.tZ)("col",{width:"66"}),(0,i.tZ)("col",{width:"48"}),(0,i.tZ)("col",{width:"48"}),(0,i.tZ)("col",{width:"48"}),(0,i.tZ)("col",{width:"48"})]}),(0,i.tZ)("thead",{children:(0,i.BX)("tr",{children:[B.map((e,t)=>"scoreCreep"===e.value&&"ARENA"===L?(0,i.tZ)("th",{}):(0,i.tZ)(N.Bp,{scope:"col",onClick:()=>el(e.value),variant:er.key===e.value?"active":void 0,order:er.order,align:"championsSummonerRank"===e.value||"name"===e.value?"left":null,children:m(e.title)},"defaultSortList-".concat(t))),A.map((e,t)=>z?(0,i.tZ)("th",{}):(0,i.tZ)(N.Bp,{scope:"col",className:("scoreDmgDealt"===e.value||"scoreDmgTaken"===e.value)&&"word-keep",onClick:()=>el(e.value),variant:er.key===e.value?"active":void 0,order:er.order,children:m(e.title)},"rankedSortList-".concat(t)))]})}),(0,i.tZ)("tbody",{children:(null==ea?void 0:ea.length)?ea.map((e,t)=>{var n,a;return(0,i.BX)("tr",{children:[(0,i.tZ)(N.Td,{align:"left",variant:"championsSummonerRank"===er.key?"active":void 0,className:"rank",children:e.championsSummonerRank}),(0,i.tZ)(N.Td,{variant:"name"===er.key?"active":void 0,children:(0,i.BX)("div",{className:"champion-container",children:[(0,i.tZ)("div",{className:"summoner-image",children:(0,i.tZ)(b(),{href:"/champions/".concat(h[e.id].key.toLowerCase()),target:"_blank",rel:"noreferrer",children:(0,i.tZ)(x.Z,{width:32,height:32,src:h[e.id].image_url,alt:h[e.id].name})})}),(0,i.tZ)("div",{className:"summoner-name",children:(0,i.tZ)(b(),{href:"/champions/".concat(h[e.id].key.toLowerCase()),target:"_blank",rel:"noreferrer",children:h[e.id].name})})]})}),(0,i.tZ)(N.Td,{variant:"gameWinRate"===er.key?"active":void 0,children:Z<=2||0===e.win&&0===e.lose?(0,i.BX)(i.HY,{children:[e.play,m("GAMECOUNT")]}):(0,i.BX)("div",{className:"win-ratio",children:[(0,i.BX)("div",{className:"winratio-graph",children:[(0,i.tZ)("div",{className:"winratio-graph__fill left  ".concat(e.lose/e.play*100==0?"only-active":""),style:{width:"".concat(e.win/e.play*100,"%")}}),e.win/e.play*100!=0&&(0,i.tZ)("div",{className:"winratio-graph__text left",children:m("WINS_SHORT",{count:e.win})}),(0,i.tZ)("div",{className:"winratio-graph__fill right"}),e.lose/e.play*100!=0&&(0,i.tZ)("div",{className:"winratio-graph__text right",children:m("LOSSES_SHORT",{count:e.lose})})]}),(0,i.BX)("span",{className:"text  ".concat(e.win/e.play*100>=60?"red":"gray"," "),children:[(e.win/e.play*100).toFixed(0),"%"]})]})}),(0,i.tZ)(N.Td,{className:"value",variant:"kda"===er.key?"active":void 0,children:(0,i.BX)("div",{children:[(0,i.tZ)(D,{kda:e.kda,children:999===e.kda?"Perfect":"".concat(e.kda,":1")}),(0,i.BX)("div",{className:"kda",children:[(e.kill/e.play).toFixed(1)," /\xa0",(e.death/e.play).toFixed(1),"\xa0 /\xa0",(e.assist/e.play).toFixed(1)]})]})}),(0,i.tZ)(N.Td,{className:"value",variant:"scoreGold"===er.key?"active":void 0,children:"".concat(e.scoreGold.toLocaleString()).concat(isFinite(e.goldPerMin)?" (".concat(e.goldPerMin,")"):"")}),(0,i.tZ)(N.Td,{className:"value",variant:"scoreCs"===er.key?"active":void 0,children:"ARENA"===L?"":"".concat(e.scoreCreep).concat(isFinite(e.csPerMin)?" (".concat(e.csPerMin,")"):"")}),(0,i.tZ)(N.Td,{className:"value",variant:"max_kill"===er.key?"active":void 0,children:z?null:e.max_kill}),(0,i.tZ)(N.Td,{className:"value",variant:"max_death"===er.key?"active":void 0,children:z?null:e.max_death}),(0,i.tZ)(N.Td,{className:"value",variant:"scoreDmgDealt"===er.key?"active":void 0,children:z?null:null===(n=e.scoreDmgDealt)||void 0===n?void 0:n.toLocaleString()}),(0,i.tZ)(N.Td,{className:"value",variant:"scoreDmgTaken"===er.key?"active":void 0,children:z?null:null===(a=e.scoreDmgTaken)||void 0===a?void 0:a.toLocaleString()}),(0,i.tZ)(N.Td,{className:"value",variant:"double_kill"===er.key?"active":void 0,children:z?null:e.double_kill?e.double_kill:null}),(0,i.tZ)(N.Td,{className:"value",variant:"triple_kill"===er.key?"active":void 0,children:z?null:e.triple_kill?e.triple_kill:null}),(0,i.tZ)(N.Td,{className:"value",variant:"quadra_kill"===er.key?"active":void 0,children:z?null:e.quadra_kill?e.quadra_kill:null}),(0,i.tZ)(N.Td,{className:"value",variant:"penta_kill"===er.key?"active":void 0,children:z?null:e.penta_kill?e.penta_kill:null})]},"tableitem-".concat(t))}):null})]}):(0,i.tZ)("tbody",{children:(0,i.tZ)("tr",{children:(0,i.tZ)(N.Td,{valign:"middle",children:(0,i.tZ)(F,{})})})})]})]})})}let K=(0,h.Z)("div",{target:"eaie9sn5"})("margin-top:10px;.filter-container{padding:0 12px;display:flex;align-items:center;> div + div{margin-left:4px;}}thead th{box-sizing:border-box;}tbody td{color:",(0,S.bB)("color","gray500"),";font-size:12px;&.rank{color:",(0,S.bB)("color","gray400"),';}&.champion{padding:0;}&.cs{font-family:"Roboto",sans-serif;}.champion-container{display:flex;align-items:center;width:32px;}.summoner-image{flex-basis:32px;a{display:block;width:32px;img{border-radius:50%;}}}}/*  그래프 */\n  .win-ratio{text-align:left;display:flex;align-items:center;padding:0 8px;box-sizing:border-box;}.winratio-graph{flex:1;position:relative;display:inline-block;height:20px;vertical-align:middle;&.winratio-graph__mobile{width:100%;}}/*  그래프 색 */\n  .winratio-graph__fill{position:absolute;left:0;top:0;height:100%;border-radius:4px;&.left{background:',(0,S.bB)("background","main500"),";border-top-right-radius:0;border-bottom-right-radius:0;z-index:1;&.only-active{border-top-right-radius:4px;border-bottom-right-radius:4px;}}&.right{width:100%;background:",(0,S.bB)("background","red500"),';}}/*  그래프 텍스트 */\n  .winratio-graph__text{position:absolute;top:3px;height:100%;line-height:15px;font-size:11px;color:#fff;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;z-index:1;&.left{left:4px;text-align:left;z-index:1;}&.right{right:4px;text-align:right;}}.text{flex-basis:40px;vertical-align:middle;font-weight:normal;text-align:center;font-family:"Roboto",sans-serif;&.gray{color:',(0,S.bB)("color","gray600"),";}&.red{color:",(0,S.bB)("color","red600"),";}}");function z(e){var t,n,r,o;let{data:c,isMobileMode:s}=e,{t:m}=(0,l.$G)("messages"),{query:{region:u}}=(0,g.useRouter)(),{championsById:h}=c,v=c.regionSeasons[(null==c?void 0:null===(t=c.regionSeasons)||void 0===t?void 0:t.length)-1].id,f=(null===(n=c.most_champions)||void 0===n?void 0:n.season_id)?null===(r=c.most_champions)||void 0===r?void 0:r.season_id:v,[y,S]=(0,a.useState)(f),[M,R]=(0,a.useState)(!1),[B,A]=(0,a.useState)(!1),P=O.map(e=>({value:e.value,label:m(e.label)})),X=L.map(e=>({value:e.value,label:m(e.label)})),U={value:"ARENA",label:m("GLOBAL_QUEUETYPE_ARENA")},z=(y===f?X:P).concat(y>=23?[U]:[]),[G,Y]=(0,a.useState)(z[0]),[W,q]=(0,a.useState)([]),Q="NORMAL"===String(G.value)||"ARENA"===String(G.value),V=y===v,{data:$,error:j,isValidating:J,mutate:ee}=(0,p.ZP)("ARENA"===G.value?[_.Z.node.summoner.summoners.mostChampions.arena(String(u),c.summoner_id),"ARENA",c.summoner_id]:Q?[_.Z.node.summoner.summoners.mostChampions.normal(String(u),c.summoner_id),Q?"NORMAL":"Normal Not Selected",c.summoner_id]:null,Q?e=>(0,C.ZP)({url:e,method:"get"}).then(e=>e.data):null,{fallbackData:c.most_champions,dedupingInterval:0,onSuccess:e=>{let t={},n=e.champion_stats.map((e,n)=>{t={...t,[e.id]:n+1};let i=t[e.id],a=Number(e.win/e.play*100),l=(0,d.XK)(e.kill,e.death,e.assist,e.play),r=Number((e.gold_earned/e.play).toFixed(0)),o=Number(((e.minion_kill+e.neutral_minion_kill)/e.play).toFixed(1)),c=Math.round(o/(e.game_length_second/e.play/60)*10)/10,s=Math.round(r/(e.game_length_second/e.play/60)*10)/10;return{...e,championsSummonerRank:i,name:h[e.id].name,gameWinRate:a,kda:l,scoreGold:r,scoreCreep:o,csPerMin:c,goldPerMin:s}});q(n)}}),{data:et,error:en,isValidating:ei,mutate:ea}=(0,p.ZP)(Q?null:[_.Z.node.summoner.summoners.mostChampions.rank(String(u),c.summoner_id),Q?"Normal Selected":String(G.value),c.summoner_id,y],Q?null:e=>(0,C.ZP)({url:e,method:"get",params:{game_type:String(G.value),season_id:y}}).then(e=>e.data),{fallbackData:c.most_champions,dedupingInterval:0,onSuccess:e=>{!M&&B&&!e.champion_stats&&V&&(Y(z[3]),A(!1));let t={},n=e.champion_stats.map((e,n)=>{t={...t,[e.id]:n+1};let i=t[e.id],a=Number(e.win/e.play*100),l=(0,d.XK)(e.kill,e.death,e.assist,e.play),r=Number((e.gold_earned/e.play).toFixed(0)),o=Number(((e.minion_kill+e.neutral_minion_kill)/e.play).toFixed(1)),c=Math.round(o/(e.game_length_second/e.play/60)*10)/10,s=Math.round(r/(e.game_length_second/e.play/60)*10)/10,m=Number((e.damage_dealt_to_champions/e.play).toFixed(0)),u=Number((e.damage_taken/e.play).toFixed(0));return{...e,championsSummonerRank:i,name:h[e.id].name,gameWinRate:a,kda:l,scoreGold:r,scoreCreep:o,csPerMin:c,goldPerMin:s,scoreDmgDealt:m,scoreDmgTaken:u}});q(n)}}),el=Q?$:et,er=Q?j:en,eo=Q?J:ei,ed=Q?ee:ea;(0,a.useEffect)(()=>{A(!0)},[]),(0,a.useEffect)(()=>{!M&&B&&y&&ed()},[M,B,y,ed]);let{data:ec,sort:es,sortType:em}=(0,w.Z)(W,"championsSummonerRank");return(0,a.useEffect)(()=>{es(em.key,em.order)},[el]),(0,i.BX)(K,{children:[(0,i.BX)("div",{className:"filter-container",children:[(0,i.tZ)(k,{data:c,handleOnClick:e=>{Q&&Y(z[0]),R(!0),S(e),es(em.key,em.order)},activeSeasonId:y,isMobileMode:s}),(0,i.tZ)(Z.ZP,{options:z,value:G,onChange:e=>{Y(e)},isMobile:s})]}),(0,i.BX)(H,{children:[(0,i.tZ)("caption",{children:m("SUMMONER_TITLE_CHAMPION_INFO")}),er?(0,i.tZ)("tbody",{children:(0,i.tZ)("tr",{children:(0,i.tZ)(N.Td,{valign:"middle",children:(0,i.tZ)(F,{})})})}):eo?(0,i.tZ)("tbody",{children:(0,i.tZ)("tr",{children:(0,i.tZ)(N.Td,{children:(0,i.tZ)(I,{children:(0,i.tZ)(E.gb,{})})})})}):(null==el?void 0:null===(o=el.champion_stats)||void 0===o?void 0:o.length)?(0,i.BX)(i.HY,{children:[(0,i.BX)("colgroup",{children:[(0,i.tZ)("col",{width:"37"}),(0,i.tZ)("col",{width:y<=2?"auto":"32"}),(0,i.tZ)("col",{width:y<=2?"90":"auto"}),(0,i.tZ)("col",{width:"50"}),(0,i.tZ)("col",{width:"72"})]}),(0,i.tZ)("thead",{children:(0,i.tZ)("tr",{children:T.map((e,t)=>(0,i.tZ)(N.Bp,{scope:"col",onClick:()=>es(e.value),variant:em.key===e.value?"active":void 0,order:em.order,align:"championsSummonerRank"===e.value?"left":null,children:"gameWinRate"===e.value||"kda"===e.value?m(e.title):e.title},"defaultSortList-".concat(t)))})}),(0,i.tZ)("tbody",{children:(null==ec?void 0:ec.length)?ec.map((e,t)=>(0,i.BX)("tr",{children:[(0,i.tZ)(N.Td,{className:"rank",align:"left",children:e.championsSummonerRank}),(0,i.tZ)(N.Td,{className:"champion",children:(0,i.tZ)("div",{className:"champion-container",children:(0,i.tZ)("div",{className:"summoner-image",children:(0,i.tZ)(b(),{href:"/champions/".concat(h[e.id].key.toLowerCase()),target:"_blank",rel:"noreferrer",children:(0,i.tZ)(x.Z,{width:32,height:32,src:h[e.id].image_url,alt:h[e.id].name})})})})}),(0,i.tZ)(N.Td,{children:y<=2||0===e.win&&0===e.lose?(0,i.BX)(i.HY,{children:[e.play,m("GAMECOUNT")]}):(0,i.BX)("div",{className:"win-ratio",children:[(0,i.BX)("div",{className:"winratio-graph",children:[(0,i.tZ)("div",{className:"winratio-graph__fill left  ".concat(e.lose/e.play*100==0?"only-active":""),style:{width:"".concat(e.win/e.play*100,"%")}}),e.win/e.play*100!=0&&(0,i.tZ)("div",{className:"winratio-graph__text left",children:m("WINS_SHORT",{count:e.win})}),(0,i.tZ)("div",{className:"winratio-graph__fill right"}),e.lose/e.play*100!=0&&(0,i.tZ)("div",{className:"winratio-graph__text right",children:m("LOSSES_SHORT",{count:e.lose})})]}),(0,i.BX)("div",{className:"text ".concat(e.win/e.play*100>=60?"red":"gray"),children:[(e.win/e.play*100).toFixed(0),"%"]})]})}),(0,i.tZ)(N.Td,{children:(0,i.tZ)(D,{kda:e.kda,children:999===e.kda?"Perfect":"".concat(e.kda,":1")})}),(0,i.tZ)(N.Td,{className:"cs",children:"".concat(e.scoreCreep).concat(isFinite(e.csPerMin)?" (".concat(e.csPerMin,")"):"")})]},"tableitem-".concat(t))):null})]}):(0,i.tZ)("tbody",{children:(0,i.tZ)("tr",{children:(0,i.tZ)(N.Td,{valign:"middle",children:(0,i.tZ)(F,{})})})})]})]})}var G=n(84343),Y=n(4643),W=n(76646),q=n(27483);let Q=u()(()=>Promise.resolve().then(n.bind(n,51597)),{loadableGenerated:{webpack:()=>[51597]},ssr:!1}),V=(0,h.Z)("div",{target:"el5n36d0"})("position:relative;background-color:",(0,S.bB)("background-color","gray0"),";");function $(e){let{data:t,extra:n,isMobileMode:a}=e,{web:l}=W.default,r=(0,d.uo)(t.name);return(0,i.BX)(i.HY,{children:[!r&&(0,i.tZ)(Q,{placementId:l.summoner.richmedia,richMedia:!0}),(0,i.BX)(V,{id:"content-header",children:[(0,i.tZ)(G.Z,{data:t,extra:n}),(0,i.tZ)(Y.Z,{summonerId:t.summoner_id})]}),!r&&(0,i.tZ)(q.mD,{id:"banner-container",children:(0,i.tZ)(Q,{placementId:l.summoner.atf,hybridBanner:!0})}),(0,i.tZ)(U,{data:t,isMobileMode:a}),!r&&(0,i.tZ)(q.Nw,{children:(0,i.tZ)(Q,{placementId:l.summoner.champion.before_footer})})]})}let j=u()(()=>Promise.resolve().then(n.bind(n,51597)),{loadableGenerated:{webpack:()=>[51597]},ssr:!1});function J(e){let{data:t,extra:n,isMobileMode:a}=e,{mobile:l}=W.default,r=(0,d.uo)(t.name);return(0,i.BX)(i.HY,{children:[!r&&(0,i.tZ)(j,{placementId:l.summoner.champions.richmedia,richMedia:!0}),(0,i.tZ)(G.W,{data:t,extra:n}),!r&&(0,i.tZ)(q.Z0,{children:(0,i.tZ)(q.rh,{})}),(0,i.tZ)(Y.Z,{summonerId:null==t?void 0:t.summoner_id,isMobile:!0}),(0,i.tZ)(z,{data:t,isMobileMode:a}),!r&&(0,i.tZ)(q.TX,{children:(0,i.tZ)(j,{placementId:l.summoner.champions.after_lnb})})]})}var ee=!0;function et(e){let{isMobileMode:t,region:n,data:r,extra:m}=e,{t:u}=(0,l.$G)("messages");if((0,a.useEffect)(()=>{r.name&&(0,s.Q2)("__hist",{region:n,summonerName:r.name})},[r,n]),(0,d.Qr)(r))return(0,i.tZ)(c.Z,{isMobileMode:t});let h="".concat(r.name," - ").concat(u("SUMMONER_TITLE_CHAMPION_INFO")," - League of Legends");return(0,i.BX)(i.HY,{children:[(0,i.BX)(o(),{children:[(0,i.tZ)("meta",{name:"title",content:h},"title"),(0,i.tZ)("meta",{property:"og:title",content:h},"og:title"),(0,i.tZ)("title",{children:h},"title_tag")]}),t?(0,i.tZ)(J,{data:r,isMobileMode:t,extra:m}):(0,i.tZ)($,{data:r,isMobileMode:t,extra:m})]})}},66199:function(e,t,n){"use strict";var i=n(67294);t.Z=(e,t,n)=>{let[a,l]=(0,i.useState)(e),[r,o]=(0,i.useState)({key:null!=t?t:"",order:null!=n?n:-1});return(0,i.useEffect)(()=>{e&&(()=>{if("positionTier"===r.key){let t=[...e].sort((e,t)=>{let n=e.positionWinRate<t.positionWinRate?1:-1;return n*r.order}),n=[...t].sort((e,t)=>{let n=e.positionTier>t.positionTier?1:-1;return n*r.order});l(n.reverse());return}if("positionRank"===r.key){let t=[...e].filter(e=>void 0!==e.positionRank),n=[...e].filter(e=>void 0===e.positionRank),i=t.sort((e,t)=>{let n=e.positionRank<t.positionRank?-1:1;return n*r.order});l([...i.reverse(),...n]);return}if("championsSummonerRank"===r.key){let t=[...e].sort((e,t)=>{let n=e.championsSummonerRank<t.championsSummonerRank?-1:1;return n*r.order});l(t.reverse());return}let t=[...e].filter(e=>void 0!==e[r.key]),n=[...e].filter(e=>void 0===e[r.key]),i=t.sort((e,t)=>{let n=e[r.key]>t[r.key]?1:-1;return n*r.order});l([...i,...n])})()},[r,e]),{data:a,sort:(e,t)=>{let n=t||r.order;e===r.key&&(n=t||(-1===n?1:-1)),o({key:e,order:n})},sortType:r}}}},function(e){e.O(0,[8277,33,452,9774,2888,179],function(){return e(e.s=7689)}),_N_E=e.O()}]);