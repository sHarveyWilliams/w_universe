Vue.component("goods-list-element", {
    props: ["good"],
    template: `
        <div class="vertical-list-element" @click.prevent="divClick" v-show="good.show">
            <input type="checkbox" id="good.label" class="vertical-list-element-checkbox" value="good.id" v-model="good.checked">
            <div class="good-checkbox-label">{{ good.name }}</div>
        </div>
    `,
    methods: {
        divClick: function () {
            this.good.checked = !this.good.checked
        }
    }
});

Vue.component("search-slider", {
    props: ["slider"],
    template: `
        <div class="slider-box">
            <label for="slider.id" class="search-slider-label">{{ slider.label }}</label>
            <input id="slider.id" class="good-search-slider" type="range" min="0" max="100" v-model.number="slider.value">
        </div>
    `
});

Vue.component("suppliers-list-element", {
    data: function () {
        return {
            active: false
        }
    },
    props: ["supplier"],
    template: `
        <div class="supplier-box">
            <div class="supplier-button" @click="buttonClicked">
                <h3 class="supplier-name">{{ supplier.name }}</h3>
            </div>
            
            <div class="supplier-addition" v-show="active">
                <div class="supplier-data">
                    <div class="supplier-data-element">Email: {{ supplier.email }}</div>
                    <div class="supplier-data-element">Phone: {{ supplier.phone }}</div>
                    <div class="supplier-data-element">Address: {{ supplier.address }}</div>
                </div>
                
                <div class="supplier-goods-list">
                    <component is="supplier-goods-list-element" v-for="sup_good in supplier.goods" 
                               :key="supplier.id + sup_good.name" :good="sup_good.name"></component>
                </div>
            </div>
        </div>
    `,
    methods: {
        buttonClicked: function () {
            this.active = !this.active;
        }
    }
});

Vue.component("supplier-goods-list-element", {
    props: ["good"],
    template: `
        <div class="supplier-goods-list-element">{{ good }}</div>
    `
});

new Vue({
    el: '#app',
    data: {
        active: true,
        sliders: [
            {id: "cost", label: "Цена", value: 0},
            {id: "quality", label: "Качество", value: 0},
            {id: "speed", label: "Скорость доставки", value: 0},
            {id: "rating", label: "Рейтинг", value: 0},
        ],
        goodsSearchInput: "",
        goods: [],
        suppliers: []
    },
    mounted: function () {
        let goodies = JSON.parse(this.$el.attributes.goodslist.value);
        this.goods = goodies.goods.sort(function (a, b) {
            return a["name"].localeCompare(b["name"]);
        });

        this.debouncedGetGoods = _.debounce(this.getGoods, 500)
    },
    watch: {
        goodsSearchInput: function (newInput, oldInput) {
            this.debouncedGetGoods()
        }
    },
    methods: {
        getGoods: function () {
            if (this.goodsSearchInput === "") {
                for (let good of this.goods) {
                    good.show = true;
                }
            } else {
                for (let good of this.goods) {
                    good.show = good.name.toLowerCase().includes(this.goodsSearchInput);
                }
            }
        },
        searchDelivery: function () {
            let settings = {"needable_goods": [], "sliders": {}};

            for (let good of this.goods) {
                if (good.checked) {
                    settings.needable_goods.push(good.id);
                }
            }

            for (let slider of this.sliders) {
                settings.sliders[slider.id] = slider.value / 100;
            }

            let vm = this;

            axios.post("/getDelivery", {"settings": settings})
                .then(function (response) {
                    vm.suppliers = response.data.delivery;
                })
                .catch(function (error) {
                    console.log(error);
                })
        }
    }
});
