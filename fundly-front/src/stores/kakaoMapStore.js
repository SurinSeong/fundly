// src/stores/mapStore.js
import { defineStore } from 'pinia'

export const useMapStore = defineStore('map', {
  state: () => ({
    map: null,
    ps: null,
    infowindow: null,
    mapData: [],
    bankData: [],
    selectedDo: '',
    selectedSi: '',
    selectedBank: '',
  }),
  actions: {
    async initMap(mapContainerId) {
      // 동적으로 스크립트 로드

      if (!window.kakao) {
        await new Promise((resolve) => {
          const script = document.createElement('script')
          script.src = `//dapi.kakao.com/v2/maps/sdk.js?appkey=${import.meta.env.VITE_APP_KEY}&libraries=services&autoload=false`
          script.onload = () => {
            window.kakao.maps.load(resolve)
          }
          document.head.appendChild(script)
        })
      } else {
        await new Promise((resolve) => {
          window.kakao.maps.load(resolve)
        })
      }

      const kakao = window.kakao
      const mapOption = {
        center: new kakao.maps.LatLng(37.4978, 127.02786),
        level: 4,
        mapTypeId: kakao.maps.MapTypeId.ROADMAP,
      }

      this.map = new kakao.maps.Map(document.getElementById(mapContainerId), mapOption)
      this.ps = new kakao.maps.services.Places()
      this.infowindow = new kakao.maps.InfoWindow({ zIndex: 1 })
    },

    async loadData() {
      const res = await fetch('/data.json')
      const data = await res.json()

      this.mapData = data.mapInfo
      this.bankData = data.bankInfo
    },

    async search() {
      const query = `${this.selectedDo} ${this.selectedSi} ${this.selectedBank}`
      this.ps.keywordSearch(query, (results, status) => {
        if (status === kakao.maps.services.Status.OK) {
          const bounds = new kakao.maps.LatLngBounds()
          results.forEach((place) => {
            const marker = new kakao.maps.Marker({
              map: this.map,
              position: new kakao.maps.LatLng(place.y, place.x),
            })
            kakao.maps.event.addListener(marker, 'click', () => {
              this.infowindow.setContent(
                `<div style="padding:5px; font-size:12px;">${place.place_name}</div>`,
              )
              this.infowindow.open(this.map, marker)
            })
            bounds.extend(new kakao.maps.LatLng(place.y, place.x))
          })
          this.map.setBounds(bounds)
        }
      })
    },
  },
})
